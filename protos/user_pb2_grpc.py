# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import user_pb2 as protos_dot_user__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_profile = channel.unary_unary(
                '/user.User/get_profile',
                request_serializer=protos_dot_user__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_user__pb2.UserProfileResponse.FromString,
                )
        self.update_profile = channel.unary_unary(
                '/user.User/update_profile',
                request_serializer=protos_dot_user__pb2.UpdateProfileRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.BaseResponse.FromString,
                )
        self.upload_avatar = channel.unary_unary(
                '/user.User/upload_avatar',
                request_serializer=protos_dot_user__pb2.UploadAvatarRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.UploadAvatarResponse.FromString,
                )
        self.request_change_password = channel.unary_unary(
                '/user.User/request_change_password',
                request_serializer=protos_dot_user__pb2.RequestChangePasswordReq.SerializeToString,
                response_deserializer=protos_dot_user__pb2.RequestChangePasswordRes.FromString,
                )
        self.change_password = channel.unary_unary(
                '/user.User/change_password',
                request_serializer=protos_dot_user__pb2.ChangePasswordRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.BaseResponse.FromString,
                )
        self.update_status = channel.unary_unary(
                '/user.User/update_status',
                request_serializer=protos_dot_user__pb2.SetUserStatusRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.BaseResponse.FromString,
                )
        self.ping_request = channel.unary_unary(
                '/user.User/ping_request',
                request_serializer=protos_dot_user__pb2.PingRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.BaseResponse.FromString,
                )
        self.get_clients_status = channel.unary_unary(
                '/user.User/get_clients_status',
                request_serializer=protos_dot_user__pb2.GetClientsStatusRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.GetClientsStatusResponse.FromString,
                )
        self.delete_account = channel.unary_unary(
                '/user.User/delete_account',
                request_serializer=protos_dot_user__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_user__pb2.BaseResponse.FromString,
                )
        self.get_user_info = channel.unary_unary(
                '/user.User/get_user_info',
                request_serializer=protos_dot_user__pb2.GetUserRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.UserInfoResponse.FromString,
                )
        self.search_user = channel.unary_unary(
                '/user.User/search_user',
                request_serializer=protos_dot_user__pb2.SearchUserRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.SearchUserResponse.FromString,
                )
        self.get_users = channel.unary_unary(
                '/user.User/get_users',
                request_serializer=protos_dot_user__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_user__pb2.GetUsersResponse.FromString,
                )
        self.find_user_by_email = channel.unary_unary(
                '/user.User/find_user_by_email',
                request_serializer=protos_dot_user__pb2.FindUserByEmailRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.UserInfoResponse.FromString,
                )
        self.get_mfa_state = channel.unary_unary(
                '/user.User/get_mfa_state',
                request_serializer=protos_dot_user__pb2.MfaGetStateRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.MfaStateResponse.FromString,
                )
        self.enable_mfa = channel.unary_unary(
                '/user.User/enable_mfa',
                request_serializer=protos_dot_user__pb2.MfaChangingStateRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.MfaBaseResponse.FromString,
                )
        self.disable_mfa = channel.unary_unary(
                '/user.User/disable_mfa',
                request_serializer=protos_dot_user__pb2.MfaChangingStateRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.MfaBaseResponse.FromString,
                )
        self.mfa_auth_challenge = channel.unary_unary(
                '/user.User/mfa_auth_challenge',
                request_serializer=protos_dot_user__pb2.MfaAuthChallengeRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.MfaAuthChallengeResponse.FromString,
                )
        self.mfa_validate_password = channel.unary_unary(
                '/user.User/mfa_validate_password',
                request_serializer=protos_dot_user__pb2.MfaValidatePasswordRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.MfaBaseResponse.FromString,
                )
        self.mfa_validate_otp = channel.unary_unary(
                '/user.User/mfa_validate_otp',
                request_serializer=protos_dot_user__pb2.MfaValidateOtpRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.MfaBaseResponse.FromString,
                )
        self.mfa_resend_otp = channel.unary_unary(
                '/user.User/mfa_resend_otp',
                request_serializer=protos_dot_user__pb2.MfaResendOtpRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.MfaBaseResponse.FromString,
                )
        self.workspace_update_display_name = channel.unary_unary(
                '/user.User/workspace_update_display_name',
                request_serializer=protos_dot_user__pb2.WorkspaceUpdateDisplayNameRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.BaseResponse.FromString,
                )
        self.workspace_find_user_by_email = channel.unary_unary(
                '/user.User/workspace_find_user_by_email',
                request_serializer=protos_dot_user__pb2.FindUserByEmailRequest.SerializeToString,
                response_deserializer=protos_dot_user__pb2.UserInfoResponse.FromString,
                )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_profile(self, request, context):
        """----- FROM MY ACCOUNT -----
        => profile api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_profile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upload_avatar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def request_change_password(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_password(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ping_request(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_clients_status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_account(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_user_info(self, request, context):
        """----- FROM OTHER ACCOUNT -----
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def search_user(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_users(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def find_user_by_email(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_mfa_state(self, request, context):
        """----- MFA ENABLE FLOW -----
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enable_mfa(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable_mfa(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mfa_auth_challenge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mfa_validate_password(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mfa_validate_otp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mfa_resend_otp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def workspace_update_display_name(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def workspace_find_user_by_email(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_profile': grpc.unary_unary_rpc_method_handler(
                    servicer.get_profile,
                    request_deserializer=protos_dot_user__pb2.Empty.FromString,
                    response_serializer=protos_dot_user__pb2.UserProfileResponse.SerializeToString,
            ),
            'update_profile': grpc.unary_unary_rpc_method_handler(
                    servicer.update_profile,
                    request_deserializer=protos_dot_user__pb2.UpdateProfileRequest.FromString,
                    response_serializer=protos_dot_user__pb2.BaseResponse.SerializeToString,
            ),
            'upload_avatar': grpc.unary_unary_rpc_method_handler(
                    servicer.upload_avatar,
                    request_deserializer=protos_dot_user__pb2.UploadAvatarRequest.FromString,
                    response_serializer=protos_dot_user__pb2.UploadAvatarResponse.SerializeToString,
            ),
            'request_change_password': grpc.unary_unary_rpc_method_handler(
                    servicer.request_change_password,
                    request_deserializer=protos_dot_user__pb2.RequestChangePasswordReq.FromString,
                    response_serializer=protos_dot_user__pb2.RequestChangePasswordRes.SerializeToString,
            ),
            'change_password': grpc.unary_unary_rpc_method_handler(
                    servicer.change_password,
                    request_deserializer=protos_dot_user__pb2.ChangePasswordRequest.FromString,
                    response_serializer=protos_dot_user__pb2.BaseResponse.SerializeToString,
            ),
            'update_status': grpc.unary_unary_rpc_method_handler(
                    servicer.update_status,
                    request_deserializer=protos_dot_user__pb2.SetUserStatusRequest.FromString,
                    response_serializer=protos_dot_user__pb2.BaseResponse.SerializeToString,
            ),
            'ping_request': grpc.unary_unary_rpc_method_handler(
                    servicer.ping_request,
                    request_deserializer=protos_dot_user__pb2.PingRequest.FromString,
                    response_serializer=protos_dot_user__pb2.BaseResponse.SerializeToString,
            ),
            'get_clients_status': grpc.unary_unary_rpc_method_handler(
                    servicer.get_clients_status,
                    request_deserializer=protos_dot_user__pb2.GetClientsStatusRequest.FromString,
                    response_serializer=protos_dot_user__pb2.GetClientsStatusResponse.SerializeToString,
            ),
            'delete_account': grpc.unary_unary_rpc_method_handler(
                    servicer.delete_account,
                    request_deserializer=protos_dot_user__pb2.Empty.FromString,
                    response_serializer=protos_dot_user__pb2.BaseResponse.SerializeToString,
            ),
            'get_user_info': grpc.unary_unary_rpc_method_handler(
                    servicer.get_user_info,
                    request_deserializer=protos_dot_user__pb2.GetUserRequest.FromString,
                    response_serializer=protos_dot_user__pb2.UserInfoResponse.SerializeToString,
            ),
            'search_user': grpc.unary_unary_rpc_method_handler(
                    servicer.search_user,
                    request_deserializer=protos_dot_user__pb2.SearchUserRequest.FromString,
                    response_serializer=protos_dot_user__pb2.SearchUserResponse.SerializeToString,
            ),
            'get_users': grpc.unary_unary_rpc_method_handler(
                    servicer.get_users,
                    request_deserializer=protos_dot_user__pb2.Empty.FromString,
                    response_serializer=protos_dot_user__pb2.GetUsersResponse.SerializeToString,
            ),
            'find_user_by_email': grpc.unary_unary_rpc_method_handler(
                    servicer.find_user_by_email,
                    request_deserializer=protos_dot_user__pb2.FindUserByEmailRequest.FromString,
                    response_serializer=protos_dot_user__pb2.UserInfoResponse.SerializeToString,
            ),
            'get_mfa_state': grpc.unary_unary_rpc_method_handler(
                    servicer.get_mfa_state,
                    request_deserializer=protos_dot_user__pb2.MfaGetStateRequest.FromString,
                    response_serializer=protos_dot_user__pb2.MfaStateResponse.SerializeToString,
            ),
            'enable_mfa': grpc.unary_unary_rpc_method_handler(
                    servicer.enable_mfa,
                    request_deserializer=protos_dot_user__pb2.MfaChangingStateRequest.FromString,
                    response_serializer=protos_dot_user__pb2.MfaBaseResponse.SerializeToString,
            ),
            'disable_mfa': grpc.unary_unary_rpc_method_handler(
                    servicer.disable_mfa,
                    request_deserializer=protos_dot_user__pb2.MfaChangingStateRequest.FromString,
                    response_serializer=protos_dot_user__pb2.MfaBaseResponse.SerializeToString,
            ),
            'mfa_auth_challenge': grpc.unary_unary_rpc_method_handler(
                    servicer.mfa_auth_challenge,
                    request_deserializer=protos_dot_user__pb2.MfaAuthChallengeRequest.FromString,
                    response_serializer=protos_dot_user__pb2.MfaAuthChallengeResponse.SerializeToString,
            ),
            'mfa_validate_password': grpc.unary_unary_rpc_method_handler(
                    servicer.mfa_validate_password,
                    request_deserializer=protos_dot_user__pb2.MfaValidatePasswordRequest.FromString,
                    response_serializer=protos_dot_user__pb2.MfaBaseResponse.SerializeToString,
            ),
            'mfa_validate_otp': grpc.unary_unary_rpc_method_handler(
                    servicer.mfa_validate_otp,
                    request_deserializer=protos_dot_user__pb2.MfaValidateOtpRequest.FromString,
                    response_serializer=protos_dot_user__pb2.MfaBaseResponse.SerializeToString,
            ),
            'mfa_resend_otp': grpc.unary_unary_rpc_method_handler(
                    servicer.mfa_resend_otp,
                    request_deserializer=protos_dot_user__pb2.MfaResendOtpRequest.FromString,
                    response_serializer=protos_dot_user__pb2.MfaBaseResponse.SerializeToString,
            ),
            'workspace_update_display_name': grpc.unary_unary_rpc_method_handler(
                    servicer.workspace_update_display_name,
                    request_deserializer=protos_dot_user__pb2.WorkspaceUpdateDisplayNameRequest.FromString,
                    response_serializer=protos_dot_user__pb2.BaseResponse.SerializeToString,
            ),
            'workspace_find_user_by_email': grpc.unary_unary_rpc_method_handler(
                    servicer.workspace_find_user_by_email,
                    request_deserializer=protos_dot_user__pb2.FindUserByEmailRequest.FromString,
                    response_serializer=protos_dot_user__pb2.UserInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_profile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/get_profile',
            protos_dot_user__pb2.Empty.SerializeToString,
            protos_dot_user__pb2.UserProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_profile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/update_profile',
            protos_dot_user__pb2.UpdateProfileRequest.SerializeToString,
            protos_dot_user__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upload_avatar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/upload_avatar',
            protos_dot_user__pb2.UploadAvatarRequest.SerializeToString,
            protos_dot_user__pb2.UploadAvatarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def request_change_password(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/request_change_password',
            protos_dot_user__pb2.RequestChangePasswordReq.SerializeToString,
            protos_dot_user__pb2.RequestChangePasswordRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def change_password(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/change_password',
            protos_dot_user__pb2.ChangePasswordRequest.SerializeToString,
            protos_dot_user__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/update_status',
            protos_dot_user__pb2.SetUserStatusRequest.SerializeToString,
            protos_dot_user__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ping_request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/ping_request',
            protos_dot_user__pb2.PingRequest.SerializeToString,
            protos_dot_user__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_clients_status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/get_clients_status',
            protos_dot_user__pb2.GetClientsStatusRequest.SerializeToString,
            protos_dot_user__pb2.GetClientsStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_account(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/delete_account',
            protos_dot_user__pb2.Empty.SerializeToString,
            protos_dot_user__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_user_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/get_user_info',
            protos_dot_user__pb2.GetUserRequest.SerializeToString,
            protos_dot_user__pb2.UserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def search_user(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/search_user',
            protos_dot_user__pb2.SearchUserRequest.SerializeToString,
            protos_dot_user__pb2.SearchUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_users(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/get_users',
            protos_dot_user__pb2.Empty.SerializeToString,
            protos_dot_user__pb2.GetUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def find_user_by_email(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/find_user_by_email',
            protos_dot_user__pb2.FindUserByEmailRequest.SerializeToString,
            protos_dot_user__pb2.UserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_mfa_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/get_mfa_state',
            protos_dot_user__pb2.MfaGetStateRequest.SerializeToString,
            protos_dot_user__pb2.MfaStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def enable_mfa(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/enable_mfa',
            protos_dot_user__pb2.MfaChangingStateRequest.SerializeToString,
            protos_dot_user__pb2.MfaBaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def disable_mfa(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/disable_mfa',
            protos_dot_user__pb2.MfaChangingStateRequest.SerializeToString,
            protos_dot_user__pb2.MfaBaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mfa_auth_challenge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/mfa_auth_challenge',
            protos_dot_user__pb2.MfaAuthChallengeRequest.SerializeToString,
            protos_dot_user__pb2.MfaAuthChallengeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mfa_validate_password(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/mfa_validate_password',
            protos_dot_user__pb2.MfaValidatePasswordRequest.SerializeToString,
            protos_dot_user__pb2.MfaBaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mfa_validate_otp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/mfa_validate_otp',
            protos_dot_user__pb2.MfaValidateOtpRequest.SerializeToString,
            protos_dot_user__pb2.MfaBaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mfa_resend_otp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/mfa_resend_otp',
            protos_dot_user__pb2.MfaResendOtpRequest.SerializeToString,
            protos_dot_user__pb2.MfaBaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def workspace_update_display_name(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/workspace_update_display_name',
            protos_dot_user__pb2.WorkspaceUpdateDisplayNameRequest.SerializeToString,
            protos_dot_user__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def workspace_find_user_by_email(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/workspace_find_user_by_email',
            protos_dot_user__pb2.FindUserByEmailRequest.SerializeToString,
            protos_dot_user__pb2.UserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
