# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/workspace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16protos/workspace.proto\x12\tworkspace\"\x1d\n\x0c\x42\x61seResponse\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"0\n\x14WorkspaceInfoRequest\x12\x18\n\x10workspace_domain\x18\x01 \x01(\t\"&\n\x15WorkspaceInfoResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"\x17\n\x15LeaveWorkspaceRequest2\xb2\x01\n\tWorkspace\x12U\n\x0eworkspace_info\x12\x1f.workspace.WorkspaceInfoRequest\x1a .workspace.WorkspaceInfoResponse\"\x00\x12N\n\x0fleave_workspace\x12 .workspace.LeaveWorkspaceRequest\x1a\x17.workspace.BaseResponse\"\x00\x62\x06proto3')



_BASERESPONSE = DESCRIPTOR.message_types_by_name['BaseResponse']
_WORKSPACEINFOREQUEST = DESCRIPTOR.message_types_by_name['WorkspaceInfoRequest']
_WORKSPACEINFORESPONSE = DESCRIPTOR.message_types_by_name['WorkspaceInfoResponse']
_LEAVEWORKSPACEREQUEST = DESCRIPTOR.message_types_by_name['LeaveWorkspaceRequest']
BaseResponse = _reflection.GeneratedProtocolMessageType('BaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _BASERESPONSE,
  '__module__' : 'protos.workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.BaseResponse)
  })
_sym_db.RegisterMessage(BaseResponse)

WorkspaceInfoRequest = _reflection.GeneratedProtocolMessageType('WorkspaceInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEINFOREQUEST,
  '__module__' : 'protos.workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceInfoRequest)
  })
_sym_db.RegisterMessage(WorkspaceInfoRequest)

WorkspaceInfoResponse = _reflection.GeneratedProtocolMessageType('WorkspaceInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEINFORESPONSE,
  '__module__' : 'protos.workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.WorkspaceInfoResponse)
  })
_sym_db.RegisterMessage(WorkspaceInfoResponse)

LeaveWorkspaceRequest = _reflection.GeneratedProtocolMessageType('LeaveWorkspaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEAVEWORKSPACEREQUEST,
  '__module__' : 'protos.workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.LeaveWorkspaceRequest)
  })
_sym_db.RegisterMessage(LeaveWorkspaceRequest)

_WORKSPACE = DESCRIPTOR.services_by_name['Workspace']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BASERESPONSE._serialized_start=37
  _BASERESPONSE._serialized_end=66
  _WORKSPACEINFOREQUEST._serialized_start=68
  _WORKSPACEINFOREQUEST._serialized_end=116
  _WORKSPACEINFORESPONSE._serialized_start=118
  _WORKSPACEINFORESPONSE._serialized_end=156
  _LEAVEWORKSPACEREQUEST._serialized_start=158
  _LEAVEWORKSPACEREQUEST._serialized_end=181
  _WORKSPACE._serialized_start=184
  _WORKSPACE._serialized_end=362
# @@protoc_insertion_point(module_scope)
