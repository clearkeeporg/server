import logging

import grpc

from protos import group_pb2_grpc

logger = logging.getLogger(__name__)


class ClientGroup:
    def __init__(self, workspace_domain):
        self.stub = self.grpc_stub(workspace_domain)

    def grpc_stub(self, workspace_domain):
        channel = grpc.insecure_channel(workspace_domain)
        return group_pb2_grpc.GroupStub(channel)

    def create_group_workspace(self, request):
        try:
            response = self.stub.create_group_workspace(request)
            return response
        except Exception as e:
            logger.error(e, exc_info=True)
            return None

    def add_member(self, request):
        try:
            response = self.stub.add_member(request)
            return response
        except Exception as e:
            logger.error(e, exc_info=True)
            return None

    def workspace_add_member(self, request):
        try:
            response = self.stub.workspace_add_member(request)
            return response
        except Exception as e:
            logger.error(e, exc_info=True)
            return None

    def get_group(self, request):
        try:
            response = self.stub.get_group(request)
            return response
        except Exception as e:
            logger.error(e, exc_info=True)
            return None

    def leave_group(self, request):
        try:
            response = self.stub.leave_group(request)
            return response
        except Exception as e:
            logger.error(e, exc_info=True)
            return None

    def workspace_leave_group(self, request):
        try:
            response = self.stub.workspace_leave_group(request)
            return response
        except Exception as e:
            logger.error(e, exc_info=True)
            return None

    def workspace_notify_deactive_member(self, request):
        try:
            response = self.stub.workspace_notify_deactive_member(request)
            return response
        except Exception as e:
            logger.error(e, exc_info=True)
            return None
