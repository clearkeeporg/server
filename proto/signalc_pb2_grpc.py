# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import signalc_pb2 as proto_dot_signalc__pb2


class SignalKeyDistributionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterBundleKey = channel.unary_unary(
                '/signalc.SignalKeyDistribution/RegisterBundleKey',
                request_serializer=proto_dot_signalc__pb2.SignalRegisterKeysRequest.SerializeToString,
                response_deserializer=proto_dot_signalc__pb2.BaseResponse.FromString,
                )
        self.GetKeyBundleByUserId = channel.unary_unary(
                '/signalc.SignalKeyDistribution/GetKeyBundleByUserId',
                request_serializer=proto_dot_signalc__pb2.SignalKeysUserRequest.SerializeToString,
                response_deserializer=proto_dot_signalc__pb2.SignalKeysUserResponse.FromString,
                )
        self.Subscribe = channel.unary_unary(
                '/signalc.SignalKeyDistribution/Subscribe',
                request_serializer=proto_dot_signalc__pb2.SubscribeAndListenRequest.SerializeToString,
                response_deserializer=proto_dot_signalc__pb2.BaseResponse.FromString,
                )
        self.Listen = channel.unary_stream(
                '/signalc.SignalKeyDistribution/Listen',
                request_serializer=proto_dot_signalc__pb2.SubscribeAndListenRequest.SerializeToString,
                response_deserializer=proto_dot_signalc__pb2.Publication.FromString,
                )
        self.Publish = channel.unary_unary(
                '/signalc.SignalKeyDistribution/Publish',
                request_serializer=proto_dot_signalc__pb2.PublishRequest.SerializeToString,
                response_deserializer=proto_dot_signalc__pb2.BaseResponse.FromString,
                )


class SignalKeyDistributionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterBundleKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetKeyBundleByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Listen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SignalKeyDistributionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterBundleKey': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterBundleKey,
                    request_deserializer=proto_dot_signalc__pb2.SignalRegisterKeysRequest.FromString,
                    response_serializer=proto_dot_signalc__pb2.BaseResponse.SerializeToString,
            ),
            'GetKeyBundleByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKeyBundleByUserId,
                    request_deserializer=proto_dot_signalc__pb2.SignalKeysUserRequest.FromString,
                    response_serializer=proto_dot_signalc__pb2.SignalKeysUserResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=proto_dot_signalc__pb2.SubscribeAndListenRequest.FromString,
                    response_serializer=proto_dot_signalc__pb2.BaseResponse.SerializeToString,
            ),
            'Listen': grpc.unary_stream_rpc_method_handler(
                    servicer.Listen,
                    request_deserializer=proto_dot_signalc__pb2.SubscribeAndListenRequest.FromString,
                    response_serializer=proto_dot_signalc__pb2.Publication.SerializeToString,
            ),
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=proto_dot_signalc__pb2.PublishRequest.FromString,
                    response_serializer=proto_dot_signalc__pb2.BaseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'signalc.SignalKeyDistribution', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SignalKeyDistribution(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterBundleKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signalc.SignalKeyDistribution/RegisterBundleKey',
            proto_dot_signalc__pb2.SignalRegisterKeysRequest.SerializeToString,
            proto_dot_signalc__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetKeyBundleByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signalc.SignalKeyDistribution/GetKeyBundleByUserId',
            proto_dot_signalc__pb2.SignalKeysUserRequest.SerializeToString,
            proto_dot_signalc__pb2.SignalKeysUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signalc.SignalKeyDistribution/Subscribe',
            proto_dot_signalc__pb2.SubscribeAndListenRequest.SerializeToString,
            proto_dot_signalc__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Listen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/signalc.SignalKeyDistribution/Listen',
            proto_dot_signalc__pb2.SubscribeAndListenRequest.SerializeToString,
            proto_dot_signalc__pb2.Publication.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/signalc.SignalKeyDistribution/Publish',
            proto_dot_signalc__pb2.PublishRequest.SerializeToString,
            proto_dot_signalc__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
