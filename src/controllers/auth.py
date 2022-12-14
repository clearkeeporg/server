import srp

import protos.auth_pb2 as auth_messages
from middlewares.permission import *
from middlewares.request_logged import *
from src.controllers.base import BaseController
from src.services.auth import AuthService
from src.services.group import GroupService
from src.services.message import MessageService
from src.services.notify_inapp import NotifyInAppService
from src.services.signal import SignalService
from src.services.user import UserService
from src.models.user import AuthSource, InvalidAuthSourceException
from utils.config import *

import logging
import asyncio
logger = logging.getLogger(__name__)
class AuthController(BaseController):
    def __init__(self, *kwargs):
        self.service = AuthService()
        self.user_service = UserService()

    @request_logged
    async def login_challenge(self, request, context):
        try:
            email = request.email
            user_info = self.user_service.get_user_by_auth_source(email, "account")
            if not user_info:
                raise Exception(Message.AUTH_USER_NOT_FOUND)
            password_verifier = bytes.fromhex(user_info.password_verifier)
            salt = bytes.fromhex(user_info.salt)
            client_public = bytes.fromhex(request.client_public)

            srv = srp.Verifier(email, salt, password_verifier, client_public)
            s, B = srv.get_challenge()

            server_private = srv.get_ephemeral_secret().hex()
            logger.info(server_private)
            user_info.srp_server_private = server_private
            user_info.update()

            public_challenge_b = B.hex()
            auth_challenge_res = auth_messages.AuthChallengeRes(
                salt=user_info.salt,
                public_challenge_b=public_challenge_b
            )
            return auth_challenge_res

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTHENTICATION_FAILED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_authenticate(self, request, context):
        try:
            user_name = request.user_name
            exists_user = self.service.get_user_by_email(user_name)
            client_session_key_proof = request.client_session_key_proof
            user_info = self.user_service.get_user_by_id(exists_user["id"])

            if not user_info:
                raise Exception(Message.AUTH_USER_NOT_FOUND)
            password_verifier = bytes.fromhex(user_info.password_verifier)
            salt = bytes.fromhex(user_info.salt)
            client_session_key_proof_bytes = bytes.fromhex(client_session_key_proof)

            srv = srp.Verifier(
                            username=user_name,
                            bytes_s=salt,
                            bytes_v=password_verifier,
                            bytes_A=bytes.fromhex(request.client_public),
                            bytes_b=bytes.fromhex(user_info.srp_server_private)
                        )
            srv.verify_session(client_session_key_proof_bytes)
            authenticated = srv.authenticated()

            if not authenticated:
                raise Exception(Message.AUTHENTICATION_FAILED)

            token = self.service.token(user_name, user_info.password_verifier)
            if token:
                user_id = user_info.id
                mfa_state = self.user_service.get_mfa_state(user_id=user_id)

                if not mfa_state:
                    client_key_obj = SignalService().peer_get_client_key(user_id)
                    client_key_peer = auth_messages.PeerGetClientKeyResponse(
                                            clientId=user_id,
                                            workspace_domain=get_owner_workspace_domain(),
                                            registrationId=client_key_obj.registration_id,
                                            deviceId=client_key_obj.device_id,
                                            identityKeyPublic=client_key_obj.identity_key_public,
                                            preKeyId=client_key_obj.prekey_id,
                                            preKey=client_key_obj.prekey,
                                            signedPreKeyId=client_key_obj.signed_prekey_id,
                                            signedPreKey=client_key_obj.signed_prekey,
                                            signedPreKeySignature=client_key_obj.signed_prekey_signature,
                                            identityKeyEncrypted=client_key_obj.identity_key_encrypted
                                        )
                    self.user_service.update_last_login(user_id=user_id)
                    auth_message = auth_messages.AuthRes(
                        workspace_domain=get_owner_workspace_domain(),
                        workspace_name=get_system_config()['server_name'],
                        access_token=token['access_token'],
                        expires_in=token['expires_in'],
                        refresh_expires_in=token['refresh_expires_in'],
                        refresh_token=token['refresh_token'],
                        token_type=token['token_type'],
                        session_state=token['session_state'],
                        scope=token['scope'],
                        salt=user_info.salt,
                        client_key_peer = client_key_peer,
                        iv_parameter=user_info.iv_parameter
                    )
                else:
                    pre_access_token = self.service.create_otp_service(user_id)
                    auth_message = auth_messages.AuthRes(
                        workspace_domain=get_owner_workspace_domain(),
                        workspace_name=get_system_config()['server_name'],
                        sub=user_id,
                        pre_access_token=pre_access_token,
                        require_action="mfa_validate_otp"
                    )
                return auth_message
        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_google(self, request, context):
        try:
            user_name, user_id, is_registered_pincode = self.service.google_login(request.id_token)
            require_action_mess = "verify_pincode" if not is_registered_pincode else "register_pincode"
            if require_action_mess == "verify_pincode":
                reset_pincode_token = self.service.hash_pre_access_token(user_name, "reset_pincode")
            else:
                reset_pincode_token = ""
            auth_challenge_res = auth_messages.SocialLoginRes(
                                    user_name=user_name,
                                    require_action=require_action_mess,
                                    reset_pincode_token=reset_pincode_token
                                )
            return auth_challenge_res
        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_office(self, request, context):
        try:
            user_name, user_id, is_registered_pincode = self.service.office_login(request.access_token)
            user_info = self.user_service.get_user_by_id(user_id)
            require_action_mess = "verify_pincode" if not is_registered_pincode else "register_pincode"
            if require_action_mess == "verify_pincode":
                reset_pincode_token = self.service.hash_pre_access_token(user_name, "reset_pincode")
            else:
                reset_pincode_token = ""
            auth_challenge_res = auth_messages.SocialLoginRes(
                                    user_name=user_name,
                                    require_action=require_action_mess,
                                    reset_pincode_token=reset_pincode_token
                                )
            return auth_challenge_res

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_facebook(self, request, context):
        try:
            user_name, user_id, is_registered_pincode = self.service.facebook_login(request.access_token)
            user_info = self.user_service.get_user_by_id(user_id)
            require_action_mess = "verify_pincode" if not is_registered_pincode else "register_pincode"
            if require_action_mess == "verify_pincode":
                reset_pincode_token = self.service.hash_pre_access_token(user_name, "reset_pincode")
            else:
                reset_pincode_token = ""
            auth_challenge_res = auth_messages.SocialLoginRes(
                                    user_name=user_name,
                                    require_action=require_action_mess,
                                    reset_pincode_token=reset_pincode_token
                                )
            return auth_challenge_res
        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_apple(self, request, context):
        try:
            user_name, user_id, is_registered_pincode = self.service.apple_login(request.id_token, request.end_user_env)
            require_action_mess = "verify_pincode" if not is_registered_pincode else "register_pincode"
            if require_action_mess == "verify_pincode":
                reset_pincode_token = self.service.hash_pre_access_token(user_name, "reset_pincode")
            else:
                reset_pincode_token = ""
            auth_challenge_res = auth_messages.SocialLoginRes(
                                    user_name=user_name,
                                    require_action=require_action_mess,
                                    reset_pincode_token=reset_pincode_token
                                )
            return auth_challenge_res
        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_social_challange(self, request, context):
        try:
            user_name = request.user_name
            exists_user = self.service.get_user_by_email(user_name)
            user_info = self.user_service.get_user_by_id(exists_user["id"])
            if not user_info:
                raise Exception(Message.AUTH_USER_NOT_FOUND)
            password_verifier = bytes.fromhex(user_info.password_verifier)
            salt = bytes.fromhex(user_info.salt)
            client_public = bytes.fromhex(request.client_public)

            srv = srp.Verifier(user_name, salt, password_verifier, client_public)
            s, B = srv.get_challenge()

            server_private = srv.get_ephemeral_secret().hex()
            logger.info(server_private)
            user_info.srp_server_private = server_private
            user_info.update()

            public_challenge_b = B.hex()
            auth_challenge_res = auth_messages.AuthChallengeRes(
                salt=user_info.salt,
                public_challenge_b=public_challenge_b
            )
            return auth_challenge_res

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTHENTICATION_FAILED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def register_srp(self, request, context):
        # check exist user
        try:
            email = request.email
            display_name = request.display_name
            password_verifier = request.password_verifier
            salt = request.salt
            iv_parameter = request.iv_parameter

            exists_user = self.service.get_user_by_email(email)
            if exists_user:
                user_info = UserService().get_user_by_id(exists_user["id"])
                try:
                    user_info.check_auth_source(AuthSource.ACCOUNT)
                except InvalidAuthSourceException as e:
                    raise Exception(Message.INVALID_ACCOUNT_AUTH_SOURCE)
                raise Exception(Message.REGISTER_USER_ALREADY_EXISTS)

            # register new user
            new_user_id = self.service.register_srp_user(email, password_verifier, display_name)

            if new_user_id:
                # create new user in database
                UserService().create_new_user_srp(new_user_id, email, password_verifier, salt, iv_parameter, display_name, AuthSource.ACCOUNT)
            else:
                self.service.delete_user(new_user_id)
                raise Exception(Message.REGISTER_USER_FAILED)
            try:
                SignalService().peer_register_client_key(new_user_id, request.client_key_peer)
            except Exception:
                self.service.delete_user(new_user_id)
                UserService().delete_user(new_user_id)
                raise Exception(Message.REGISTER_USER_FAILED)

            return auth_messages.RegisterSRPRes()

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.REGISTER_USER_FAILED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def forgot_password(self, request, context):
        try:
            self.service.send_forgot_password(request.email)
            return auth_messages.BaseResponse()

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def forgot_password_update(self, request, context):
        try:
            logger.info("from email {}".format(request.email))
            user_info = self.user_service.get_user_by_auth_source(request.email, "account")
            old_user_id = user_info.id
            success_status = self.service.verify_hash_pre_access_token(old_user_id, request.pre_access_token, "forgot_password")
            if not success_status:
                raise Exception(Message.CHANGE_PASSWORD_FAILED)
            new_user_id = await self.service.forgot_user(request.email, request.password_verifier, user_info.display_name)
            try:
                await GroupService().forgot_peer_groups_for_client(user_info)
            except Exception as e:
                logger.error("cannot send notify to other group")
                logger.error(e, exc_info=True)
            await GroupService().member_forgot_password_in_group(user_info)
            SignalService().delete_client_peer_key(old_user_id)
            if new_user_id:
                # create new user in database
                UserService().forgot_user(user_info, new_user_id, request.password_verifier, request.salt, request.iv_parameter)
            else:
                self.service.delete_user(new_user_id)
                raise Exception(Message.REGISTER_USER_FAILED)
            try:
                SignalService().peer_register_client_key(new_user_id, request.client_key_peer)
            except Exception:
                self.service.delete_user(new_user_id)
                UserService().delete_user(new_user_id)
                raise Exception(Message.REGISTER_USER_FAILED)

            token = self.service.token(request.email, request.password_verifier)
            if token:
                client_key_obj = request.client_key_peer
                client_key_peer = auth_messages.PeerGetClientKeyResponse(
                                        clientId=new_user_id,
                                        workspace_domain=get_owner_workspace_domain(),
                                        registrationId=client_key_obj.registrationId,
                                        deviceId=client_key_obj.deviceId,
                                        identityKeyPublic=client_key_obj.identityKeyPublic,
                                        preKeyId=client_key_obj.preKeyId,
                                        preKey=client_key_obj.preKey,
                                        signedPreKeyId=client_key_obj.signedPreKeyId,
                                        signedPreKey=client_key_obj.signedPreKey,
                                        signedPreKeySignature=client_key_obj.signedPreKeySignature,
                                        identityKeyEncrypted=client_key_obj.identityKeyEncrypted
                                    )
                self.user_service.update_last_login(user_id=new_user_id)
                auth_message = auth_messages.AuthRes(
                    workspace_domain=get_owner_workspace_domain(),
                    workspace_name=get_system_config()['server_name'],
                    access_token=token['access_token'],
                    expires_in=token['expires_in'],
                    refresh_expires_in=token['refresh_expires_in'],
                    refresh_token=token['refresh_token'],
                    token_type=token['token_type'],
                    session_state=token['session_state'],
                    scope=token['scope'],
                    salt=request.salt,
                    client_key_peer=client_key_peer,
                    iv_parameter=request.iv_parameter
                )
            else:
                raise Exception(Message.AUTH_USER_NOT_FOUND)
            return auth_message

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.CHANGE_PASSWORD_FAILED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @auth_required
    @request_logged
    async def logout(self, request, context):
        try:
            header_data = dict(context.invocation_metadata())
            introspect_token = KeyCloakUtils.introspect_token(header_data['access_token'])
            user_id = introspect_token['sub']
            device_id = request.device_id
            refresh_token = request.refresh_token
            self.service.remove_token(client_id=user_id, device_id=device_id)
            MessageService().un_subscribe(user_id, device_id)
            NotifyInAppService().un_subscribe(user_id, device_id)
            self.service.logout(refresh_token)
            return auth_messages.BaseResponse()

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    async def validate_otp(self, request, context):
        try:
            success_status  = self.service.verify_otp(request.user_id, request.pre_access_token, request.otp_code)
            if not success_status:
                raise Exception(Message.AUTH_USER_NOT_FOUND)

            user_info = self.user_service.get_user_by_id(request.user_id)
            token = self.service.token(user_info.email, user_info.password_verifier)
            introspect_token = KeyCloakUtils.introspect_token(token['access_token'])
            require_action = ""
            client_key_obj = SignalService().peer_get_client_key(request.user_id)
            client_key_peer = auth_messages.PeerGetClientKeyResponse(
                                    clientId=request.user_id,
                                    workspace_domain=get_owner_workspace_domain(),
                                    registrationId=client_key_obj.registration_id,
                                    deviceId=client_key_obj.device_id,
                                    identityKeyPublic=client_key_obj.identity_key_public,
                                    preKeyId=client_key_obj.prekey_id,
                                    preKey=client_key_obj.prekey,
                                    signedPreKeyId=client_key_obj.signed_prekey_id,
                                    signedPreKey=client_key_obj.signed_prekey,
                                    signedPreKeySignature=client_key_obj.signed_prekey_signature,
                                    identityKeyEncrypted=client_key_obj.identity_key_encrypted
                                )
            self.user_service.update_last_login(user_id=request.user_id)
            return auth_messages.AuthRes(
                workspace_domain=get_owner_workspace_domain(),
                workspace_name=get_system_config()['server_name'],
                access_token=token["access_token"],
                expires_in=token['expires_in'],
                refresh_expires_in=token['refresh_expires_in'],
                refresh_token=token['refresh_token'],
                token_type=token['token_type'],
                session_state=token['session_state'],
                scope=token['scope'],
                require_action = require_action,
                salt=user_info.salt,
                client_key_peer=client_key_peer,
                iv_parameter=user_info.iv_parameter
            )

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.GET_MFA_STATE_FALED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    async def resend_otp(self, request, context):
        try:
            pre_access_token = self.service.resend_otp(request.user_id, request.pre_access_token)
            return auth_messages.MfaResendOtpRes(
                                success=True,
                                pre_access_token=pre_access_token
                            )

        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.GET_MFA_STATE_FALED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def register_pincode(self, request, context):
        try:
            exists_user = self.service.get_user_by_email(request.user_name)
            if not exists_user:
                raise Exception(Message.REGISTER_CLIENT_SIGNAL_KEY_FAILED)
            user_info = self.user_service.get_user_by_id(exists_user["id"])
            if user_info.password_verifier is not None:
                raise Exception(Message.REGISTER_USER_ALREADY_EXISTS)
            salt = request.salt
            self.user_service.change_password(request, None, request.hash_pincode, exists_user['id'])
            # using hash_pincode as password for social user
            try:
                SignalService().peer_register_client_key(exists_user['id'], request.client_key_peer)
            except Exception as e:
                logger.error(e, exc_info=True)
            try:
                UserService().update_hash_pin(exists_user['id'], request.hash_pincode, request.salt, request.iv_parameter)
            except Exception as e:
                logger.error(e, exc_info=True)
                ## TODO: revert change_password
                SignalService().delete_client_peer_key(exists_user['id'])
                raise Message.get_error_object(Message.REGISTER_CLIENT_SIGNAL_KEY_FAILED)
            require_action = ""
            client_key_obj = request.client_key_peer
            client_key_peer = auth_messages.PeerGetClientKeyResponse(
                                    clientId=exists_user['id'],
                                    workspace_domain=get_owner_workspace_domain(),
                                    registrationId=client_key_obj.registrationId,
                                    deviceId=client_key_obj.deviceId,
                                    identityKeyPublic=client_key_obj.identityKeyPublic,
                                    preKeyId=client_key_obj.preKeyId,
                                    preKey=client_key_obj.preKey,
                                    signedPreKeyId=client_key_obj.signedPreKeyId,
                                    signedPreKey=client_key_obj.signedPreKey,
                                    signedPreKeySignature=client_key_obj.signedPreKeySignature,
                                    identityKeyEncrypted=client_key_obj.identityKeyEncrypted
                                )
            token = self.service.token(request.user_name, request.hash_pincode)
            introspect_token = KeyCloakUtils.introspect_token(token['access_token'])
            self.user_service.update_last_login(user_id=introspect_token['sub'])
            return auth_messages.AuthRes(
                workspace_domain=get_owner_workspace_domain(),
                workspace_name=get_system_config()['server_name'],
                access_token=token["access_token"],
                expires_in=token['expires_in'],
                refresh_expires_in=token['refresh_expires_in'],
                refresh_token=token['refresh_token'],
                token_type=token['token_type'],
                session_state=token['session_state'],
                scope=token['scope'],
                salt=request.salt,
                client_key_peer = client_key_peer,
                iv_parameter=request.iv_parameter
            )
        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.REGISTER_CLIENT_SIGNAL_KEY_FAILED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def reset_pincode(self, request, context):
        try:
            success_status = self.service.verify_hash_pre_access_token(request.user_name, request.reset_pincode_token, "reset_pincode")
            exists_user = self.service.get_user_by_email(request.user_name)
            if not exists_user:
                raise Exception(Message.USER_NOT_FOUND)
            if not success_status:
                raise Exception(Message.REGISTER_CLIENT_SIGNAL_KEY_FAILED)
            self.user_service.change_password(request, None, request.hash_pincode, exists_user["id"])
            await self.service.notify_myself_reset_pincode(exists_user["id"])
            old_client_key_peer = SignalService().peer_get_client_key(exists_user["id"])
            SignalService().client_update_peer_key(exists_user["id"], request.client_key_peer)
            await GroupService().member_reset_pincode_in_group(exists_user["id"])
            try:
                salt, iv_parameter = UserService().update_hash_pin(exists_user["id"], request.hash_pincode, request.salt, request.iv_parameter)
            except Exception as e:
                logger.error(e, exc_info=True)
                SignalService().client_update_peer_key(exists_user["id"], old_client_key_peer)
                raise Message.get_error_object(Message.REGISTER_CLIENT_SIGNAL_KEY_FAILED)
            client_key_obj = request.client_key_peer
            client_key_peer = auth_messages.PeerGetClientKeyResponse(
                                    clientId=exists_user["id"],
                                    workspace_domain=get_owner_workspace_domain(),
                                    registrationId=client_key_obj.registrationId,
                                    deviceId=client_key_obj.deviceId,
                                    identityKeyPublic=client_key_obj.identityKeyPublic,
                                    preKeyId=client_key_obj.preKeyId,
                                    preKey=client_key_obj.preKey,
                                    signedPreKeyId=client_key_obj.signedPreKeyId,
                                    signedPreKey=client_key_obj.signedPreKey,
                                    signedPreKeySignature=client_key_obj.signedPreKeySignature,
                                    identityKeyEncrypted=client_key_obj.identityKeyEncrypted
                                )
            # logout all device before get new token for user after updated new key
            user_sessions = KeyCloakUtils.get_sessions(user_id=exists_user["id"])
            for user_session in user_sessions:
                KeyCloakUtils.remove_session(session_id=user_session['id'])
            token = self.service.token(request.user_name, request.hash_pincode)
            introspect_token = KeyCloakUtils.introspect_token(token['access_token'])
            return auth_messages.AuthRes(
                workspace_domain=get_owner_workspace_domain(),
                workspace_name=get_system_config()['server_name'],
                access_token=token["access_token"],
                expires_in=token['expires_in'],
                refresh_expires_in=token['refresh_expires_in'],
                refresh_token=token['refresh_token'],
                token_type=token['token_type'],
                session_state=token['session_state'],
                scope=token['scope'],
                salt=salt,
                client_key_peer=client_key_peer,
                iv_parameter=iv_parameter
            )
        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.REGISTER_CLIENT_SIGNAL_KEY_FAILED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
                context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
                context.set_code(grpc.StatusCode.INTERNAL)

    async def verify_pincode(self, request, context):
        try:
            exists_user = self.service.get_user_by_email(request.user_name)
            user_info = self.user_service.get_user_by_id(exists_user["id"])
            if not user_info:
                raise Exception(Message.AUTH_USER_NOT_FOUND)
            password_verifier = bytes.fromhex(user_info.password_verifier)
            salt = bytes.fromhex(user_info.salt)
            client_session_key_proof = request.client_session_key_proof
            client_session_key_proof_bytes = bytes.fromhex(client_session_key_proof)

            srv = srp.Verifier(
                        username=request.user_name,
                        bytes_s=salt,
                        bytes_v=password_verifier,
                        bytes_A=bytes.fromhex(request.client_public),
                        bytes_b=bytes.fromhex(user_info.srp_server_private)
                    )
            srv.verify_session(client_session_key_proof_bytes)
            authenticated = srv.authenticated()

            if not authenticated:
                raise Exception(Message.AUTHENTICATION_FAILED)

            token = self.service.token(request.user_name, user_info.password_verifier)
            introspect_token = KeyCloakUtils.introspect_token(token['access_token'])
            if not token:
                raise Exception(Message.VERIFY_PINCODE_FAILED)

            client_key_obj = SignalService().peer_get_client_key(introspect_token['sub'])
            client_key_peer = auth_messages.PeerGetClientKeyResponse(
                                    clientId=introspect_token['sub'],
                                    workspace_domain=get_owner_workspace_domain(),
                                    registrationId=client_key_obj.registration_id,
                                    deviceId=client_key_obj.device_id,
                                    identityKeyPublic=client_key_obj.identity_key_public,
                                    preKeyId=client_key_obj.prekey_id,
                                    preKey=client_key_obj.prekey,
                                    signedPreKeyId=client_key_obj.signed_prekey_id,
                                    signedPreKey=client_key_obj.signed_prekey,
                                    signedPreKeySignature=client_key_obj.signed_prekey_signature,
                                    identityKeyEncrypted=client_key_obj.identity_key_encrypted
                                )
            self.user_service.update_last_login(user_id=introspect_token['sub'])
            return auth_messages.AuthRes(
                workspace_domain=get_owner_workspace_domain(),
                workspace_name=get_system_config()['server_name'],
                access_token=token["access_token"],
                expires_in=token['expires_in'],
                refresh_expires_in=token['refresh_expires_in'],
                refresh_token=token['refresh_token'],
                token_type=token['token_type'],
                session_state=token['session_state'],
                scope=token['scope'],
                salt=user_info.salt,
                client_key_peer = client_key_peer,
                iv_parameter=user_info.iv_parameter
            )
        except Exception as e:
            logger.error(e, exc_info=True)
            if not e.args or e.args[0] not in Message.msg_dict:
                errors = [Message.get_error_object(Message.VERIFY_PINCODE_FAILED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def refresh_token(self, request, context):
        def call_refresh_token():
            return self.service.refresh_token(request.refresh_token)

        loop = asyncio.get_running_loop()
        try:
            token = await loop.run_in_executor(None, call_refresh_token)

            return auth_messages.RefreshTokenRes(
                access_token=token['access_token'],
                expires_in=token['expires_in'],
                refresh_expires_in=token['refresh_expires_in'],
                refresh_token=token['refresh_token'],
                token_type=token['token_type'],
                session_state=token['session_state'],
                scope=token['scope']
            )
        except Exception as e:
            if not e.args or e.args[0] not in Message.msg_dict:
                logger.warning(e,exc_info=True)
                raise
            else:
                logger.info(e)
                errors = [Message.get_error_object(e.args[0])]
                context.set_details(json.dumps(
                    errors, default=lambda x: x.__dict__))
                context.set_code(grpc.StatusCode.INTERNAL)
