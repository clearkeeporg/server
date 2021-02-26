# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/stream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/stream.proto',
  package='stream',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13protos/stream.proto\x12\x06stream\"\x1d\n\rStreamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1e\n\x0bStreamReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\x94\x01\n\x07Greeter\x12\x42\n\x12UnaryUnaryGreeting\x12\x15.stream.StreamRequest\x1a\x13.stream.StreamReply\"\x00\x12\x45\n\x13UnaryStreamGreeting\x12\x15.stream.StreamRequest\x1a\x13.stream.StreamReply\"\x00\x30\x01\x62\x06proto3'
)




_STREAMREQUEST = _descriptor.Descriptor(
  name='StreamRequest',
  full_name='stream.StreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='stream.StreamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=31,
  serialized_end=60,
)


_STREAMREPLY = _descriptor.Descriptor(
  name='StreamReply',
  full_name='stream.StreamReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='stream.StreamReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=62,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['StreamRequest'] = _STREAMREQUEST
DESCRIPTOR.message_types_by_name['StreamReply'] = _STREAMREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMREQUEST,
  '__module__' : 'protos.stream_pb2'
  # @@protoc_insertion_point(class_scope:stream.StreamRequest)
  })
_sym_db.RegisterMessage(StreamRequest)

StreamReply = _reflection.GeneratedProtocolMessageType('StreamReply', (_message.Message,), {
  'DESCRIPTOR' : _STREAMREPLY,
  '__module__' : 'protos.stream_pb2'
  # @@protoc_insertion_point(class_scope:stream.StreamReply)
  })
_sym_db.RegisterMessage(StreamReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='stream.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=95,
  serialized_end=243,
  methods=[
  _descriptor.MethodDescriptor(
    name='UnaryUnaryGreeting',
    full_name='stream.Greeter.UnaryUnaryGreeting',
    index=0,
    containing_service=None,
    input_type=_STREAMREQUEST,
    output_type=_STREAMREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UnaryStreamGreeting',
    full_name='stream.Greeter.UnaryStreamGreeting',
    index=1,
    containing_service=None,
    input_type=_STREAMREQUEST,
    output_type=_STREAMREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
