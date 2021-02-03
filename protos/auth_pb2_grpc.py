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
        self.login = channel.unary_unary(
                '/auth.Auth/login',
                request_serializer=protos_dot_auth__pb2.AuthReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.AuthRes.FromString,
                )
        self.register = channel.unary_unary(
                '/auth.Auth/register',
                request_serializer=protos_dot_auth__pb2.RegisterReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.RegisterRes.FromString,
                )
        self.fogot_password = channel.unary_unary(
                '/auth.Auth/fogot_password',
                request_serializer=protos_dot_auth__pb2.FogotPassWord.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.BaseResponse.FromString,
                )
        self.logout = channel.unary_unary(
                '/auth.Auth/logout',
                request_serializer=protos_dot_auth__pb2.LogoutReq.SerializeToString,
                response_deserializer=protos_dot_auth__pb2.BaseResponse.FromString,
                )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file."""

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fogot_password(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=protos_dot_auth__pb2.AuthReq.FromString,
                    response_serializer=protos_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=protos_dot_auth__pb2.RegisterReq.FromString,
                    response_serializer=protos_dot_auth__pb2.RegisterRes.SerializeToString,
            ),
            'fogot_password': grpc.unary_unary_rpc_method_handler(
                    servicer.fogot_password,
                    request_deserializer=protos_dot_auth__pb2.FogotPassWord.FromString,
                    response_serializer=protos_dot_auth__pb2.BaseResponse.SerializeToString,
            ),
            'logout': grpc.unary_unary_rpc_method_handler(
                    servicer.logout,
                    request_deserializer=protos_dot_auth__pb2.LogoutReq.FromString,
                    response_serializer=protos_dot_auth__pb2.BaseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/login',
            protos_dot_auth__pb2.AuthReq.SerializeToString,
            protos_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/register',
            protos_dot_auth__pb2.RegisterReq.SerializeToString,
            protos_dot_auth__pb2.RegisterRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def fogot_password(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/fogot_password',
            protos_dot_auth__pb2.FogotPassWord.SerializeToString,
            protos_dot_auth__pb2.BaseResponse.FromString,
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
