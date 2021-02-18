# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/server_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/server_info.proto',
  package='server_info',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18protos/server_info.proto\x12\x0bserver_info\"*\n\x0cUpdateNTSReq\x12\x0c\n\x04stun\x18\x01 \x01(\t\x12\x0c\n\x04turn\x18\x02 \x01(\t\"\x1f\n\x0c\x42\x61seResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32R\n\nServerInfo\x12\x44\n\nupdate_nts\x12\x19.server_info.UpdateNTSReq\x1a\x19.server_info.BaseResponse\"\x00\x62\x06proto3'
)




_UPDATENTSREQ = _descriptor.Descriptor(
  name='UpdateNTSReq',
  full_name='server_info.UpdateNTSReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stun', full_name='server_info.UpdateNTSReq.stun', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='turn', full_name='server_info.UpdateNTSReq.turn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=83,
)


_BASERESPONSE = _descriptor.Descriptor(
  name='BaseResponse',
  full_name='server_info.BaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='server_info.BaseResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['UpdateNTSReq'] = _UPDATENTSREQ
DESCRIPTOR.message_types_by_name['BaseResponse'] = _BASERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateNTSReq = _reflection.GeneratedProtocolMessageType('UpdateNTSReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATENTSREQ,
  '__module__' : 'protos.server_info_pb2'
  # @@protoc_insertion_point(class_scope:server_info.UpdateNTSReq)
  })
_sym_db.RegisterMessage(UpdateNTSReq)

BaseResponse = _reflection.GeneratedProtocolMessageType('BaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _BASERESPONSE,
  '__module__' : 'protos.server_info_pb2'
  # @@protoc_insertion_point(class_scope:server_info.BaseResponse)
  })
_sym_db.RegisterMessage(BaseResponse)



_SERVERINFO = _descriptor.ServiceDescriptor(
  name='ServerInfo',
  full_name='server_info.ServerInfo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=118,
  serialized_end=200,
  methods=[
  _descriptor.MethodDescriptor(
    name='update_nts',
    full_name='server_info.ServerInfo.update_nts',
    index=0,
    containing_service=None,
    input_type=_UPDATENTSREQ,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERINFO)

DESCRIPTOR.services_by_name['ServerInfo'] = _SERVERINFO

# @@protoc_insertion_point(module_scope)