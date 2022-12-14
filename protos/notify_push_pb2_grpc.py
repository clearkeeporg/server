# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import notify_push_pb2 as protos_dot_notify__push__pb2


class NotifyPushStub(object):
    """Method
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register_token = channel.unary_unary(
                '/notify_push.NotifyPush/register_token',
                request_serializer=protos_dot_notify__push__pb2.RegisterTokenRequest.SerializeToString,
                response_deserializer=protos_dot_notify__push__pb2.BaseResponse.FromString,
                )
        self.push_text = channel.unary_unary(
                '/notify_push.NotifyPush/push_text',
                request_serializer=protos_dot_notify__push__pb2.PushTextRequest.SerializeToString,
                response_deserializer=protos_dot_notify__push__pb2.BaseResponse.FromString,
                )
        self.push_voip = channel.unary_unary(
                '/notify_push.NotifyPush/push_voip',
                request_serializer=protos_dot_notify__push__pb2.PushVoipRequest.SerializeToString,
                response_deserializer=protos_dot_notify__push__pb2.BaseResponse.FromString,
                )


class NotifyPushServicer(object):
    """Method
    """

    def register_token(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def push_text(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def push_voip(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotifyPushServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register_token': grpc.unary_unary_rpc_method_handler(
                    servicer.register_token,
                    request_deserializer=protos_dot_notify__push__pb2.RegisterTokenRequest.FromString,
                    response_serializer=protos_dot_notify__push__pb2.BaseResponse.SerializeToString,
            ),
            'push_text': grpc.unary_unary_rpc_method_handler(
                    servicer.push_text,
                    request_deserializer=protos_dot_notify__push__pb2.PushTextRequest.FromString,
                    response_serializer=protos_dot_notify__push__pb2.BaseResponse.SerializeToString,
            ),
            'push_voip': grpc.unary_unary_rpc_method_handler(
                    servicer.push_voip,
                    request_deserializer=protos_dot_notify__push__pb2.PushVoipRequest.FromString,
                    response_serializer=protos_dot_notify__push__pb2.BaseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'notify_push.NotifyPush', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NotifyPush(object):
    """Method
    """

    @staticmethod
    def register_token(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notify_push.NotifyPush/register_token',
            protos_dot_notify__push__pb2.RegisterTokenRequest.SerializeToString,
            protos_dot_notify__push__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def push_text(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notify_push.NotifyPush/push_text',
            protos_dot_notify__push__pb2.PushTextRequest.SerializeToString,
            protos_dot_notify__push__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def push_voip(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notify_push.NotifyPush/push_voip',
            protos_dot_notify__push__pb2.PushVoipRequest.SerializeToString,
            protos_dot_notify__push__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
