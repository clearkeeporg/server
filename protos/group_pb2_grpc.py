# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import group_pb2 as protos_dot_group__pb2


class GroupStub(object):
    """Method
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create_group = channel.unary_unary(
                '/group.Group/create_group',
                request_serializer=protos_dot_group__pb2.CreateGroupRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.GroupObjectResponse.FromString,
                )
        self.create_group_workspace = channel.unary_unary(
                '/group.Group/create_group_workspace',
                request_serializer=protos_dot_group__pb2.CreateGroupWorkspaceRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.CreateGroupWorkspaceResponse.FromString,
                )
        self.get_group = channel.unary_unary(
                '/group.Group/get_group',
                request_serializer=protos_dot_group__pb2.GetGroupRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.GroupObjectResponse.FromString,
                )
        self.search_groups = channel.unary_unary(
                '/group.Group/search_groups',
                request_serializer=protos_dot_group__pb2.SearchGroupsRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.SearchGroupsResponse.FromString,
                )
        self.get_joined_groups = channel.unary_unary(
                '/group.Group/get_joined_groups',
                request_serializer=protos_dot_group__pb2.GetJoinedGroupsRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.GetJoinedGroupsResponse.FromString,
                )
        self.join_group = channel.unary_unary(
                '/group.Group/join_group',
                request_serializer=protos_dot_group__pb2.JoinGroupRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.BaseResponse.FromString,
                )
        self.add_member = channel.unary_unary(
                '/group.Group/add_member',
                request_serializer=protos_dot_group__pb2.AddMemberRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.BaseResponse.FromString,
                )
        self.leave_group = channel.unary_unary(
                '/group.Group/leave_group',
                request_serializer=protos_dot_group__pb2.LeaveGroupRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.BaseResponse.FromString,
                )
        self.workspace_add_member = channel.unary_unary(
                '/group.Group/workspace_add_member',
                request_serializer=protos_dot_group__pb2.AddMemberWorkspaceRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.AddMemberWorkspaceResponse.FromString,
                )
        self.workspace_leave_group = channel.unary_unary(
                '/group.Group/workspace_leave_group',
                request_serializer=protos_dot_group__pb2.WorkspaceLeaveGroupRequest.SerializeToString,
                response_deserializer=protos_dot_group__pb2.BaseResponse.FromString,
                )


class GroupServicer(object):
    """Method
    """

    def create_group(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_group_workspace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_group(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def search_groups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_joined_groups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def join_group(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def add_member(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def leave_group(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def workspace_add_member(self, request, context):
        """workspace call
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def workspace_leave_group(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GroupServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create_group': grpc.unary_unary_rpc_method_handler(
                    servicer.create_group,
                    request_deserializer=protos_dot_group__pb2.CreateGroupRequest.FromString,
                    response_serializer=protos_dot_group__pb2.GroupObjectResponse.SerializeToString,
            ),
            'create_group_workspace': grpc.unary_unary_rpc_method_handler(
                    servicer.create_group_workspace,
                    request_deserializer=protos_dot_group__pb2.CreateGroupWorkspaceRequest.FromString,
                    response_serializer=protos_dot_group__pb2.CreateGroupWorkspaceResponse.SerializeToString,
            ),
            'get_group': grpc.unary_unary_rpc_method_handler(
                    servicer.get_group,
                    request_deserializer=protos_dot_group__pb2.GetGroupRequest.FromString,
                    response_serializer=protos_dot_group__pb2.GroupObjectResponse.SerializeToString,
            ),
            'search_groups': grpc.unary_unary_rpc_method_handler(
                    servicer.search_groups,
                    request_deserializer=protos_dot_group__pb2.SearchGroupsRequest.FromString,
                    response_serializer=protos_dot_group__pb2.SearchGroupsResponse.SerializeToString,
            ),
            'get_joined_groups': grpc.unary_unary_rpc_method_handler(
                    servicer.get_joined_groups,
                    request_deserializer=protos_dot_group__pb2.GetJoinedGroupsRequest.FromString,
                    response_serializer=protos_dot_group__pb2.GetJoinedGroupsResponse.SerializeToString,
            ),
            'join_group': grpc.unary_unary_rpc_method_handler(
                    servicer.join_group,
                    request_deserializer=protos_dot_group__pb2.JoinGroupRequest.FromString,
                    response_serializer=protos_dot_group__pb2.BaseResponse.SerializeToString,
            ),
            'add_member': grpc.unary_unary_rpc_method_handler(
                    servicer.add_member,
                    request_deserializer=protos_dot_group__pb2.AddMemberRequest.FromString,
                    response_serializer=protos_dot_group__pb2.BaseResponse.SerializeToString,
            ),
            'leave_group': grpc.unary_unary_rpc_method_handler(
                    servicer.leave_group,
                    request_deserializer=protos_dot_group__pb2.LeaveGroupRequest.FromString,
                    response_serializer=protos_dot_group__pb2.BaseResponse.SerializeToString,
            ),
            'workspace_add_member': grpc.unary_unary_rpc_method_handler(
                    servicer.workspace_add_member,
                    request_deserializer=protos_dot_group__pb2.AddMemberWorkspaceRequest.FromString,
                    response_serializer=protos_dot_group__pb2.AddMemberWorkspaceResponse.SerializeToString,
            ),
            'workspace_leave_group': grpc.unary_unary_rpc_method_handler(
                    servicer.workspace_leave_group,
                    request_deserializer=protos_dot_group__pb2.WorkspaceLeaveGroupRequest.FromString,
                    response_serializer=protos_dot_group__pb2.BaseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'group.Group', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Group(object):
    """Method
    """

    @staticmethod
    def create_group(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/create_group',
            protos_dot_group__pb2.CreateGroupRequest.SerializeToString,
            protos_dot_group__pb2.GroupObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_group_workspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/create_group_workspace',
            protos_dot_group__pb2.CreateGroupWorkspaceRequest.SerializeToString,
            protos_dot_group__pb2.CreateGroupWorkspaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_group(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/get_group',
            protos_dot_group__pb2.GetGroupRequest.SerializeToString,
            protos_dot_group__pb2.GroupObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def search_groups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/search_groups',
            protos_dot_group__pb2.SearchGroupsRequest.SerializeToString,
            protos_dot_group__pb2.SearchGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_joined_groups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/get_joined_groups',
            protos_dot_group__pb2.GetJoinedGroupsRequest.SerializeToString,
            protos_dot_group__pb2.GetJoinedGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def join_group(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/join_group',
            protos_dot_group__pb2.JoinGroupRequest.SerializeToString,
            protos_dot_group__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def add_member(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/add_member',
            protos_dot_group__pb2.AddMemberRequest.SerializeToString,
            protos_dot_group__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def leave_group(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/leave_group',
            protos_dot_group__pb2.LeaveGroupRequest.SerializeToString,
            protos_dot_group__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def workspace_add_member(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/workspace_add_member',
            protos_dot_group__pb2.AddMemberWorkspaceRequest.SerializeToString,
            protos_dot_group__pb2.AddMemberWorkspaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def workspace_leave_group(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/workspace_leave_group',
            protos_dot_group__pb2.WorkspaceLeaveGroupRequest.SerializeToString,
            protos_dot_group__pb2.BaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
