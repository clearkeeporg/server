# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/find_user_by_email.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fprotos/find_user_by_email.proto\x12\x12\x66ind_user_by_email\":\n\x14PushEmailHashRequest\x12\x12\n\nemail_hash\x18\x01 \x01(\t\x12\x0e\n\x06server\x18\x02 \x01(\t\"\'\n\x15PushEmailHashResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"3\n\x1dGetServerFromEmailHashRequest\x12\x12\n\nemail_hash\x18\x01 \x01(\t\"\x19\n\x06Server\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"Q\n\x1eGetServerFromEmailHashResponse\x12/\n\x0bserver_list\x18\x01 \x03(\x0b\x32\x1a.find_user_by_email.Server2\x8a\x02\n\x16\x46indUserByEmailService\x12h\n\x0fpush_email_hash\x12(.find_user_by_email.PushEmailHashRequest\x1a).find_user_by_email.PushEmailHashResponse\"\x00\x12\x85\x01\n\x1aget_server_from_email_hash\x12\x31.find_user_by_email.GetServerFromEmailHashRequest\x1a\x32.find_user_by_email.GetServerFromEmailHashResponse\"\x00\x62\x06proto3')



_PUSHEMAILHASHREQUEST = DESCRIPTOR.message_types_by_name['PushEmailHashRequest']
_PUSHEMAILHASHRESPONSE = DESCRIPTOR.message_types_by_name['PushEmailHashResponse']
_GETSERVERFROMEMAILHASHREQUEST = DESCRIPTOR.message_types_by_name['GetServerFromEmailHashRequest']
_SERVER = DESCRIPTOR.message_types_by_name['Server']
_GETSERVERFROMEMAILHASHRESPONSE = DESCRIPTOR.message_types_by_name['GetServerFromEmailHashResponse']
PushEmailHashRequest = _reflection.GeneratedProtocolMessageType('PushEmailHashRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUSHEMAILHASHREQUEST,
  '__module__' : 'protos.find_user_by_email_pb2'
  # @@protoc_insertion_point(class_scope:find_user_by_email.PushEmailHashRequest)
  })
_sym_db.RegisterMessage(PushEmailHashRequest)

PushEmailHashResponse = _reflection.GeneratedProtocolMessageType('PushEmailHashResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUSHEMAILHASHRESPONSE,
  '__module__' : 'protos.find_user_by_email_pb2'
  # @@protoc_insertion_point(class_scope:find_user_by_email.PushEmailHashResponse)
  })
_sym_db.RegisterMessage(PushEmailHashResponse)

GetServerFromEmailHashRequest = _reflection.GeneratedProtocolMessageType('GetServerFromEmailHashRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERFROMEMAILHASHREQUEST,
  '__module__' : 'protos.find_user_by_email_pb2'
  # @@protoc_insertion_point(class_scope:find_user_by_email.GetServerFromEmailHashRequest)
  })
_sym_db.RegisterMessage(GetServerFromEmailHashRequest)

Server = _reflection.GeneratedProtocolMessageType('Server', (_message.Message,), {
  'DESCRIPTOR' : _SERVER,
  '__module__' : 'protos.find_user_by_email_pb2'
  # @@protoc_insertion_point(class_scope:find_user_by_email.Server)
  })
_sym_db.RegisterMessage(Server)

GetServerFromEmailHashResponse = _reflection.GeneratedProtocolMessageType('GetServerFromEmailHashResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERFROMEMAILHASHRESPONSE,
  '__module__' : 'protos.find_user_by_email_pb2'
  # @@protoc_insertion_point(class_scope:find_user_by_email.GetServerFromEmailHashResponse)
  })
_sym_db.RegisterMessage(GetServerFromEmailHashResponse)

_FINDUSERBYEMAILSERVICE = DESCRIPTOR.services_by_name['FindUserByEmailService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PUSHEMAILHASHREQUEST._serialized_start=55
  _PUSHEMAILHASHREQUEST._serialized_end=113
  _PUSHEMAILHASHRESPONSE._serialized_start=115
  _PUSHEMAILHASHRESPONSE._serialized_end=154
  _GETSERVERFROMEMAILHASHREQUEST._serialized_start=156
  _GETSERVERFROMEMAILHASHREQUEST._serialized_end=207
  _SERVER._serialized_start=209
  _SERVER._serialized_end=234
  _GETSERVERFROMEMAILHASHRESPONSE._serialized_start=236
  _GETSERVERFROMEMAILHASHRESPONSE._serialized_end=317
  _FINDUSERBYEMAILSERVICE._serialized_start=320
  _FINDUSERBYEMAILSERVICE._serialized_end=586
# @@protoc_insertion_point(module_scope)
