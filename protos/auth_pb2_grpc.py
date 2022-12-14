# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import auth_pb2 as protos_dot_auth__pb2


class AuthStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register_srp = channel.unary_unary(
                '/auth.Auth/register_srp',
                request_serializer=protos_dot_auth__pb2.RegisterSRPReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.RegisterSRPRes.FromString,
                )
        self.forgot_password = channel.unary_unary(
                '/auth.Auth/forgot_password',
                request_serializer=protos_dot_auth__pb2.ForgotPasswordReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.BaseResponse.FromString,
                )
        self.login_challenge = channel.unary_unary(
                '/auth.Auth/login_challenge',
                request_serializer=protos_dot_auth__pb2.AuthChallengeReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthChallengeRes.FromString,
                )
        self.forgot_password_update = channel.unary_unary(
                '/auth.Auth/forgot_password_update',
                request_serializer=protos_dot_auth__pb2.ForgotPasswordUpdateReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthRes.FromString,
                )
        self.login_google = channel.unary_unary(
                '/auth.Auth/login_google',
                request_serializer=protos_dot_auth__pb2.GoogleLoginReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.SocialLoginRes.FromString,
                )
        self.login_office = channel.unary_unary(
                '/auth.Auth/login_office',
                request_serializer=protos_dot_auth__pb2.OfficeLoginReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.SocialLoginRes.FromString,
                )
        self.login_facebook = channel.unary_unary(
                '/auth.Auth/login_facebook',
                request_serializer=protos_dot_auth__pb2.FacebookLoginReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.SocialLoginRes.FromString,
                )
        self.login_apple = channel.unary_unary(
                '/auth.Auth/login_apple',
                request_serializer=protos_dot_auth__pb2.AppleLoginReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.SocialLoginRes.FromString,
                )
        self.login_social_challange = channel.unary_unary(
                '/auth.Auth/login_social_challange',
                request_serializer=protos_dot_auth__pb2.AuthSocialChallengeReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthChallengeRes.FromString,
                )
        self.login_authenticate = channel.unary_unary(
                '/auth.Auth/login_authenticate',
                request_serializer=protos_dot_auth__pb2.AuthenticateReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthRes.FromString,
                )
        self.refresh_token = channel.unary_unary(
                '/auth.Auth/refresh_token',
                request_serializer=protos_dot_auth__pb2.RefreshTokenReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.RefreshTokenRes.FromString,
                )
        self.logout = channel.unary_unary(
                '/auth.Auth/logout',
                request_serializer=protos_dot_auth__pb2.LogoutReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.BaseResponse.FromString,
                )
        self.register_pincode = channel.unary_unary(
                '/auth.Auth/register_pincode',
                request_serializer=protos_dot_auth__pb2.RegisterPinCodeReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthRes.FromString,
                )
        self.verify_pincode = channel.unary_unary(
                '/auth.Auth/verify_pincode',
                request_serializer=protos_dot_auth__pb2.VerifyPinCodeReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthRes.FromString,
                )
        self.reset_pincode = channel.unary_unary(
                '/auth.Auth/reset_pincode',
                request_serializer=protos_dot_auth__pb2.ResetPinCodeReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthRes.FromString,
                )
        self.validate_otp = channel.unary_unary(
                '/auth.Auth/validate_otp',
                request_serializer=protos_dot_auth__pb2.MfaValidateOtpRequest.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthRes.FromString,
                )
        self.resend_otp = channel.unary_unary(
                '/auth.Auth/resend_otp',
                request_serializer=protos_dot_auth__pb2.MfaResendOtpReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.MfaResendOtpRes.FromString,
                )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file."""

    def register_srp(self, request, context):
        """rpc register(RegisterReq) returns (RegisterRes) {};
        rpc login(AuthReq) returns (AuthRes) {};
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def forgot_password(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login_challenge(self, request, context):
        """new flow login with srp
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def forgot_password_update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login_google(self, request, context):
        """login with social
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login_office(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login_facebook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login_apple(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login_social_challange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login_authenticate(self, request, context):
        """authenticated challange
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def refresh_token(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def logout(self, request, context):
        """logout
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def register_pincode(self, request, context):
        """pincode flow
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def verify_pincode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reset_pincode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def validate_otp(self, request, context):
        """end new flow login with srp
        mfa flow
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def resend_otp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register_srp': grpc.unary_unary_rpc_method_handler(
                    servicer.register_srp,
                    request_deserializer=protos_dot_auth__pb2.RegisterSRPReq.FromString,
                    response_serializer=protos_dot_auth__pb2.RegisterSRPRes.SerializeToString,
            ),
            'forgot_password': grpc.unary_unary_rpc_method_handler(
                    servicer.forgot_password,
                    request_deserializer=protos_dot_auth__pb2.ForgotPasswordReq.FromString,
                    response_serializer=protos_dot_auth__pb2.BaseResponse.SerializeToString,
            ),
            'login_challenge': grpc.unary_unary_rpc_method_handler(
                    servicer.login_challenge,
                    request_deserializer=protos_dot_auth__pb2.AuthChallengeReq.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthChallengeRes.SerializeToString,
            ),
            'forgot_password_update': grpc.unary_unary_rpc_method_handler(
                    servicer.forgot_password_update,
                    request_deserializer=protos_dot_auth__pb2.ForgotPasswordUpdateReq.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'login_google': grpc.unary_unary_rpc_method_handler(
                    servicer.login_google,
                    request_deserializer=protos_dot_auth__pb2.GoogleLoginReq.FromString,
                    response_serializer=protos_dot_auth__pb2.SocialLoginRes.SerializeToString,
            ),
            'login_office': grpc.unary_unary_rpc_method_handler(
                    servicer.login_office,
                    request_deserializer=protos_dot_auth__pb2.OfficeLoginReq.FromString,
                    response_serializer=protos_dot_auth__pb2.SocialLoginRes.SerializeToString,
            ),
            'login_facebook': grpc.unary_unary_rpc_method_handler(
                    servicer.login_facebook,
                    request_deserializer=protos_dot_auth__pb2.FacebookLoginReq.FromString,
                    response_serializer=protos_dot_auth__pb2.SocialLoginRes.SerializeToString,
            ),
            'login_apple': grpc.unary_unary_rpc_method_handler(
                    servicer.login_apple,
                    request_deserializer=protos_dot_auth__pb2.AppleLoginReq.FromString,
                    response_serializer=protos_dot_auth__pb2.SocialLoginRes.SerializeToString,
            ),
            'login_social_challange': grpc.unary_unary_rpc_method_handler(
                    servicer.login_social_challange,
                    request_deserializer=protos_dot_auth__pb2.AuthSocialChallengeReq.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthChallengeRes.SerializeToString,
            ),
            'login_authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.login_authenticate,
                    request_deserializer=protos_dot_auth__pb2.AuthenticateReq.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'refresh_token': grpc.unary_unary_rpc_method_handler(
                    servicer.refresh_token,
                    request_deserializer=protos_dot_auth__pb2.RefreshTokenReq.FromString,
                    response_serializer=protos_dot_auth__pb2.RefreshTokenRes.SerializeToString,
            ),
            'logout': grpc.unary_unary_rpc_method_handler(
                    servicer.logout,
                    request_deserializer=protos_dot_auth__pb2.LogoutReq.FromString,
                    response_serializer=protos_dot_auth__pb2.BaseResponse.SerializeToString,
            ),
            'register_pincode': grpc.unary_unary_rpc_method_handler(
                    servicer.register_pincode,
                    request_deserializer=protos_dot_auth__pb2.RegisterPinCodeReq.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'verify_pincode': grpc.unary_unary_rpc_method_handler(
                    servicer.verify_pincode,
                    request_deserializer=protos_dot_auth__pb2.VerifyPinCodeReq.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'reset_pincode': grpc.unary_unary_rpc_method_handler(
                    servicer.reset_pincode,
                    request_deserializer=protos_dot_auth__pb2.ResetPinCodeReq.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'validate_otp': grpc.unary_unary_rpc_method_handler(
                    servicer.validate_otp,
                    request_deserializer=protos_dot_auth__pb2.MfaValidateOtpRequest.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'resend_otp': grpc.unary_unary_rpc_method_handler(
                    servicer.resend_otp,
                    request_deserializer=protos_dot_auth__pb2.MfaResendOtpReq.FromString,
                    response_serializer=protos_dot_auth__pb2.MfaResendOtpRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def register_srp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/register_srp',
            protos_dot_auth__pb2.RegisterSRPReq.SerializeToString,
            protos_dot_auth__pb2.RegisterSRPRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def forgot_password(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/forgot_password',
            protos_dot_auth__pb2.ForgotPasswordReq.SerializeToString,
            protos_dot_auth__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login_challenge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/login_challenge',
            protos_dot_auth__pb2.AuthChallengeReq.SerializeToString,
            protos_dot_auth__pb2.AuthChallengeRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def forgot_password_update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/forgot_password_update',
            protos_dot_auth__pb2.ForgotPasswordUpdateReq.SerializeToString,
            protos_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login_google(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/login_google',
            protos_dot_auth__pb2.GoogleLoginReq.SerializeToString,
            protos_dot_auth__pb2.SocialLoginRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login_office(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/login_office',
            protos_dot_auth__pb2.OfficeLoginReq.SerializeToString,
            protos_dot_auth__pb2.SocialLoginRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login_facebook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/login_facebook',
            protos_dot_auth__pb2.FacebookLoginReq.SerializeToString,
            protos_dot_auth__pb2.SocialLoginRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login_apple(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/login_apple',
            protos_dot_auth__pb2.AppleLoginReq.SerializeToString,
            protos_dot_auth__pb2.SocialLoginRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login_social_challange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/login_social_challange',
            protos_dot_auth__pb2.AuthSocialChallengeReq.SerializeToString,
            protos_dot_auth__pb2.AuthChallengeRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login_authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/login_authenticate',
            protos_dot_auth__pb2.AuthenticateReq.SerializeToString,
            protos_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def refresh_token(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/refresh_token',
            protos_dot_auth__pb2.RefreshTokenReq.SerializeToString,
            protos_dot_auth__pb2.RefreshTokenRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/logout',
            protos_dot_auth__pb2.LogoutReq.SerializeToString,
            protos_dot_auth__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def register_pincode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/register_pincode',
            protos_dot_auth__pb2.RegisterPinCodeReq.SerializeToString,
            protos_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def verify_pincode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/verify_pincode',
            protos_dot_auth__pb2.VerifyPinCodeReq.SerializeToString,
            protos_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def reset_pincode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/reset_pincode',
            protos_dot_auth__pb2.ResetPinCodeReq.SerializeToString,
            protos_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def validate_otp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/validate_otp',
            protos_dot_auth__pb2.MfaValidateOtpRequest.SerializeToString,
            protos_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def resend_otp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/resend_otp',
            protos_dot_auth__pb2.MfaResendOtpReq.SerializeToString,
            protos_dot_auth__pb2.MfaResendOtpRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
