import protos.auth_pb2 as auth_messages
from src.controllers.base import BaseController
from src.services.auth import AuthService
from src.services.user import UserService
from src.services.message import MessageService
from src.services.notify_inapp import NotifyInAppService
from utils.encrypt import EncryptUtils
from middlewares.permission import *
from middlewares.request_logged import *
from utils.config import *


class AuthController(BaseController):
    def __init__(self, *kwargs):
        self.service = AuthService()
        self.user_service = UserService()

    @request_logged
    async def login(self, request, context):
        try:
            token = self.service.token(request.email, request.password)
            if token:
                introspect_token = KeyCloakUtils.introspect_token(token['access_token'])
                user_id = introspect_token['sub']
                mfa_state = self.user_service.get_mfa_state(user_id=user_id)
                hash_key = EncryptUtils.encoded_hash(
                    request.password, user_id
                )
                if not mfa_state:
                    ### check if login require otp check
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
                                        hash_key=hash_key
                                    )
                else:
                    otp_hash = self.service.create_otp_service(user_id)
                    auth_message = auth_messages.AuthRes(
                                        workspace_domain=get_owner_workspace_domain(),
                                        workspace_name=get_system_config()['server_name'],
                                        hash_key=hash_key,
                                        sub=user_id,
                                        otp_hash=otp_hash,
                                        require_action="mfa_validate_otp"
                                    )
                return auth_message
            else:
                raise Exception(Message.AUTH_USER_NOT_FOUND)

        except Exception as e:
            logger.error(e)
            if not e.args or e.args[0] not in Message.msg_dict:
                # basic exception dont have any args / exception raised by some library may contains some args, but will not in listed message
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_google(self, request, context):
        try:
            token = self.service.google_login(request.id_token)
            introspect_token = KeyCloakUtils.introspect_token(token['access_token'])
            if token:
                #self.user_service.update_last_login(user_id=introspect_token['sub'])
                auth_response = auth_messages.AuthRes(
                    workspace_domain=get_owner_workspace_domain(),
                    workspace_name=get_system_config()['server_name'],
                    access_token=token['access_token'],
                    expires_in=token['expires_in'],
                    hash_key=EncryptUtils.encoded_hash(introspect_token['sub'], introspect_token['sub'])
                )
                if token['refresh_token']:
                    auth_response.refresh_token = token['refresh_token']
                if token['refresh_expires_in']:
                    auth_response.refresh_expires_in = token['refresh_expires_in']
                if token['token_type']:
                    auth_response.token_type = token['token_type']
                if token['session_state']:
                    auth_response.session_state = token['session_state']
                if token['scope']:
                    auth_response.scope = token['scope']

                return auth_response
            else:
                raise Exception(Message.AUTH_USER_NOT_FOUND)

        except Exception as e:
            logger.error(e)
            if not e.args or e.args[0] not in Message.msg_dict:
                # basic exception dont have any args / exception raised by some library may contains some args, but will not in listed message
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_office(self, request, context):
        try:
            token = self.service.office_login(request.access_token)
            introspect_token = KeyCloakUtils.introspect_token(token['access_token'])
            if token:
                #self.user_service.update_last_login(user_id=introspect_token['sub'])
                auth_response = auth_messages.AuthRes(
                    workspace_domain=get_owner_workspace_domain(),
                    workspace_name=get_system_config()['server_name'],
                    access_token=token['access_token'],
                    expires_in=token['expires_in'],
                    hash_key=EncryptUtils.encoded_hash(introspect_token['sub'], introspect_token['sub'])
                )
                if token['refresh_token']:
                    auth_response.refresh_token = token['refresh_token']
                if token['refresh_expires_in']:
                    auth_response.refresh_expires_in = token['refresh_expires_in']
                if token['token_type']:
                    auth_response.token_type = token['token_type']
                if token['session_state']:
                    auth_response.session_state = token['session_state']
                if token['scope']:
                    auth_response.scope = token['scope']

                return auth_response
            else:
                raise Exception(Message.AUTH_USER_NOT_FOUND)

        except Exception as e:
            logger.error(e)
            if not e.args or e.args[0] not in Message.msg_dict:
                # basic exception dont have any args / exception raised by some library may contains some args, but will not in listed message
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def login_facebook(self, request, context):
        try:
            token = self.service.facebook_login(request.access_token)
            introspect_token = KeyCloakUtils.introspect_token(token['access_token'])
            if token:
                # self.user_service.update_last_login(user_id=introspect_token['sub'])
                auth_response = auth_messages.AuthRes(
                    workspace_domain=get_owner_workspace_domain(),
                    workspace_name=get_system_config()['server_name'],
                    access_token=token['access_token'],
                    expires_in=token['expires_in'],
                    hash_key=EncryptUtils.encoded_hash(introspect_token['sub'], introspect_token['sub'])
                )
                if token['refresh_token']:
                    auth_response.refresh_token = token['refresh_token']
                if token['refresh_expires_in']:
                    auth_response.refresh_expires_in = token['refresh_expires_in']
                if token['token_type']:
                    auth_response.token_type = token['token_type']
                if token['session_state']:
                    auth_response.session_state = token['session_state']
                if token['scope']:
                    auth_response.scope = token['scope']

                return auth_response
            else:
                raise Exception(Message.AUTH_USER_NOT_FOUND)

        except Exception as e:
            logger.error(e)
            if not e.args or e.args[0] not in Message.msg_dict:
                # basic exception dont have any args / exception raised by some library may contains some args, but will not in listed message
                errors = [Message.get_error_object(Message.AUTH_USER_NOT_FOUND)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    @request_logged
    async def register(self, request, context):
        # check exist user
        try:
            exists_user = self.service.get_user_by_email(request.email)
            if exists_user:
                raise Exception(Message.REGISTER_USER_ALREADY_EXISTS)

            # register new user
            new_user = self.service.register_user(request.email, request.password, request.display_name)

            if new_user:
                # create new user in database
                UserService().create_new_user(new_user, request.email, request.display_name,  'account')
                return auth_messages.RegisterRes(
                    base_response=auth_messages.BaseResponse(
                        success=True
                    ))
            else:
                self.service.delete_user(new_user)
                raise Exception(Message.REGISTER_USER_FAILED)
        except Exception as e:
            logger.error(e)
            errors = [Message.get_error_object(e.args[0])]
            return auth_messages.RegisterRes(
                base_response=auth_messages.BaseResponse(
                    success=False,
                    errors=auth_messages.ErrorRes(
                        code=errors[0].code,
                        message=errors[0].message
                    )
                ))

    @request_logged
    async def fogot_password(self, request, context):
        try:
            self.service.send_forgot_password(request.email)
            return auth_messages.BaseResponse(
                success=True
            )
        except Exception as e:
            logger.error(e)
            errors = [Message.get_error_object(e.args[0])]
            return auth_messages.BaseResponse(
                success=False,
                errors=auth_messages.ErrorRes(
                    code=errors[0].code,
                    message=errors[0].message
                )
            )

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
            MessageService().un_subscribe(user_id)
            NotifyInAppService().un_subscribe(user_id)
            self.service.logout(refresh_token)
            # KeyCloakUtils.remove_session(
            #     session_id=introspect_token['session_state']
            # )

            return auth_messages.BaseResponse(
                success=True
            )
        except Exception as e:
            logger.error(e)
            errors = [Message.get_error_object(e.args[0])]
            return auth_messages.BaseResponse(
                success=False,
                errors=auth_messages.ErrorRes(
                    code=errors[0].code,
                    message=errors[0].message
                )
            )

    async def validate_otp(self, request, context):
        try:
            success_status, token = self.service.verify_otp(request.user_id, request.otp_hash, request.otp_code)
            if not success_status:
                raise Exception(Message.AUTH_USER_NOT_FOUND)
            introspect_token = KeyCloakUtils.introspect_token(token["access_token"])
            require_action = ""
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
                require_action = require_action
            )

        except Exception as e:
            logger.error(e)
            if not e.args or e.args[0] not in Message.msg_dict:
                # basic exception dont have any args / exception raised by some library may contains some args, but will not in listed message
                errors = [Message.get_error_object(Message.GET_MFA_STATE_FALED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)

    async def resend_otp(self, request, context):
        try:
            otp_hash = self.service.resend_otp(request.user_id, request.otp_hash)
            return auth_messages.MfaResendOtpRes(
                                success=True,
                                otp_hash=otp_hash
                            )

        except Exception as e:
            logger.error(e)
            if not e.args or e.args[0] not in Message.msg_dict:
                # basic exception dont have any args / exception raised by some library may contains some args, but will not in listed message
                errors = [Message.get_error_object(Message.GET_MFA_STATE_FALED)]
            else:
                errors = [Message.get_error_object(e.args[0])]
            context.set_details(json.dumps(
                errors, default=lambda x: x.__dict__))
            context.set_code(grpc.StatusCode.INTERNAL)
