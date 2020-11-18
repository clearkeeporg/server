# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/signal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/signal.proto',
  package='signal',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12proto/signal.proto\x12\x06signal\"\x1f\n\x0c\x42\x61seResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xe4\x01\n\x1cPeerRegisterClientKeyRequest\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\x12\x16\n\x0eregistrationId\x18\x02 \x01(\x05\x12\x10\n\x08\x64\x65viceId\x18\x03 \x01(\x05\x12\x19\n\x11identityKeyPublic\x18\x04 \x01(\x0c\x12\x10\n\x08preKeyId\x18\x05 \x01(\x05\x12\x0e\n\x06preKey\x18\x06 \x01(\x0c\x12\x16\n\x0esignedPreKeyId\x18\x07 \x01(\x05\x12\x14\n\x0csignedPreKey\x18\x08 \x01(\x0c\x12\x1d\n\x15signedPreKeySignature\x18\t \x01(\x0c\"+\n\x17PeerGetClientKeyRequest\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\"\xe0\x01\n\x18PeerGetClientKeyResponse\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\x12\x16\n\x0eregistrationId\x18\x02 \x01(\x05\x12\x10\n\x08\x64\x65viceId\x18\x03 \x01(\x05\x12\x19\n\x11identityKeyPublic\x18\x04 \x01(\x0c\x12\x10\n\x08preKeyId\x18\x05 \x01(\x05\x12\x0e\n\x06preKey\x18\x06 \x01(\x0c\x12\x16\n\x0esignedPreKeyId\x18\x07 \x01(\x05\x12\x14\n\x0csignedPreKey\x18\x08 \x01(\x0c\x12\x1d\n\x15signedPreKeySignature\x18\t \x01(\x0c\"s\n\x1dGroupRegisterClientKeyRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x03 \x01(\x05\x12\x1d\n\x15\x63lientKeyDistribution\x18\x04 \x01(\x0c\"Y\n\x14GroupClientKeyObject\x12\x10\n\x08\x63lientId\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x03 \x01(\x05\x12\x1d\n\x15\x63lientKeyDistribution\x18\x04 \x01(\x0c\"=\n\x18GroupGetClientKeyRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\t\"]\n\x19GroupGetClientKeyResponse\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12/\n\tclientKey\x18\x02 \x01(\x0b\x32\x1c.signal.GroupClientKeyObject\".\n\x1bGroupGetAllClientKeyRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\"c\n\x1cGroupGetAllClientKeyResponse\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12\x32\n\x0clstClientKey\x18\x02 \x03(\x0b\x32\x1c.signal.GroupClientKeyObject\"m\n\x0ePublishRequest\x12\x14\n\x0c\x66romClientId\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\t\x12\x0f\n\x07groupId\x18\x03 \x01(\t\x12\x11\n\tgroupType\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\x0c\"-\n\x19SubscribeAndListenRequest\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\"X\n\x0bPublication\x12\x14\n\x0c\x66romClientId\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12\x11\n\tgroupType\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\x0c\x32\x9a\x05\n\x15SignalKeyDistribution\x12S\n\x15PeerRegisterClientKey\x12$.signal.PeerRegisterClientKeyRequest\x1a\x14.signal.BaseResponse\x12U\n\x10PeerGetClientKey\x12\x1f.signal.PeerGetClientKeyRequest\x1a .signal.PeerGetClientKeyResponse\x12U\n\x16GroupRegisterClientKey\x12%.signal.GroupRegisterClientKeyRequest\x1a\x14.signal.BaseResponse\x12X\n\x11GroupGetClientKey\x12 .signal.GroupGetClientKeyRequest\x1a!.signal.GroupGetClientKeyResponse\x12\x61\n\x14GroupGetAllClientKey\x12#.signal.GroupGetAllClientKeyRequest\x1a$.signal.GroupGetAllClientKeyResponse\x12\x44\n\tSubscribe\x12!.signal.SubscribeAndListenRequest\x1a\x14.signal.BaseResponse\x12\x42\n\x06Listen\x12!.signal.SubscribeAndListenRequest\x1a\x13.signal.Publication0\x01\x12\x37\n\x07Publish\x12\x16.signal.PublishRequest\x1a\x14.signal.BaseResponseb\x06proto3'
)




_BASERESPONSE = _descriptor.Descriptor(
  name='BaseResponse',
  full_name='signal.BaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='signal.BaseResponse.message', index=0,
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
  serialized_start=30,
  serialized_end=61,
)


_PEERREGISTERCLIENTKEYREQUEST = _descriptor.Descriptor(
  name='PeerRegisterClientKeyRequest',
  full_name='signal.PeerRegisterClientKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='signal.PeerRegisterClientKeyRequest.clientId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registrationId', full_name='signal.PeerRegisterClientKeyRequest.registrationId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='signal.PeerRegisterClientKeyRequest.deviceId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identityKeyPublic', full_name='signal.PeerRegisterClientKeyRequest.identityKeyPublic', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preKeyId', full_name='signal.PeerRegisterClientKeyRequest.preKeyId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preKey', full_name='signal.PeerRegisterClientKeyRequest.preKey', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signedPreKeyId', full_name='signal.PeerRegisterClientKeyRequest.signedPreKeyId', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signedPreKey', full_name='signal.PeerRegisterClientKeyRequest.signedPreKey', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signedPreKeySignature', full_name='signal.PeerRegisterClientKeyRequest.signedPreKeySignature', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=64,
  serialized_end=292,
)


_PEERGETCLIENTKEYREQUEST = _descriptor.Descriptor(
  name='PeerGetClientKeyRequest',
  full_name='signal.PeerGetClientKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='signal.PeerGetClientKeyRequest.clientId', index=0,
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
  serialized_start=294,
  serialized_end=337,
)


_PEERGETCLIENTKEYRESPONSE = _descriptor.Descriptor(
  name='PeerGetClientKeyResponse',
  full_name='signal.PeerGetClientKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='signal.PeerGetClientKeyResponse.clientId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registrationId', full_name='signal.PeerGetClientKeyResponse.registrationId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='signal.PeerGetClientKeyResponse.deviceId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identityKeyPublic', full_name='signal.PeerGetClientKeyResponse.identityKeyPublic', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preKeyId', full_name='signal.PeerGetClientKeyResponse.preKeyId', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preKey', full_name='signal.PeerGetClientKeyResponse.preKey', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signedPreKeyId', full_name='signal.PeerGetClientKeyResponse.signedPreKeyId', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signedPreKey', full_name='signal.PeerGetClientKeyResponse.signedPreKey', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signedPreKeySignature', full_name='signal.PeerGetClientKeyResponse.signedPreKeySignature', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=340,
  serialized_end=564,
)


_GROUPREGISTERCLIENTKEYREQUEST = _descriptor.Descriptor(
  name='GroupRegisterClientKeyRequest',
  full_name='signal.GroupRegisterClientKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='signal.GroupRegisterClientKeyRequest.groupId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='signal.GroupRegisterClientKeyRequest.clientId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='signal.GroupRegisterClientKeyRequest.deviceId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientKeyDistribution', full_name='signal.GroupRegisterClientKeyRequest.clientKeyDistribution', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=566,
  serialized_end=681,
)


_GROUPCLIENTKEYOBJECT = _descriptor.Descriptor(
  name='GroupClientKeyObject',
  full_name='signal.GroupClientKeyObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='signal.GroupClientKeyObject.clientId', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='signal.GroupClientKeyObject.deviceId', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientKeyDistribution', full_name='signal.GroupClientKeyObject.clientKeyDistribution', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=683,
  serialized_end=772,
)


_GROUPGETCLIENTKEYREQUEST = _descriptor.Descriptor(
  name='GroupGetClientKeyRequest',
  full_name='signal.GroupGetClientKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='signal.GroupGetClientKeyRequest.groupId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='signal.GroupGetClientKeyRequest.clientId', index=1,
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
  serialized_start=774,
  serialized_end=835,
)


_GROUPGETCLIENTKEYRESPONSE = _descriptor.Descriptor(
  name='GroupGetClientKeyResponse',
  full_name='signal.GroupGetClientKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='signal.GroupGetClientKeyResponse.groupId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientKey', full_name='signal.GroupGetClientKeyResponse.clientKey', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=837,
  serialized_end=930,
)


_GROUPGETALLCLIENTKEYREQUEST = _descriptor.Descriptor(
  name='GroupGetAllClientKeyRequest',
  full_name='signal.GroupGetAllClientKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='signal.GroupGetAllClientKeyRequest.groupId', index=0,
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
  serialized_start=932,
  serialized_end=978,
)


_GROUPGETALLCLIENTKEYRESPONSE = _descriptor.Descriptor(
  name='GroupGetAllClientKeyResponse',
  full_name='signal.GroupGetAllClientKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='signal.GroupGetAllClientKeyResponse.groupId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lstClientKey', full_name='signal.GroupGetAllClientKeyResponse.lstClientKey', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=980,
  serialized_end=1079,
)


_PUBLISHREQUEST = _descriptor.Descriptor(
  name='PublishRequest',
  full_name='signal.PublishRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fromClientId', full_name='signal.PublishRequest.fromClientId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='signal.PublishRequest.clientId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupId', full_name='signal.PublishRequest.groupId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupType', full_name='signal.PublishRequest.groupType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='signal.PublishRequest.message', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=1081,
  serialized_end=1190,
)


_SUBSCRIBEANDLISTENREQUEST = _descriptor.Descriptor(
  name='SubscribeAndListenRequest',
  full_name='signal.SubscribeAndListenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='signal.SubscribeAndListenRequest.clientId', index=0,
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
  serialized_start=1192,
  serialized_end=1237,
)


_PUBLICATION = _descriptor.Descriptor(
  name='Publication',
  full_name='signal.Publication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fromClientId', full_name='signal.Publication.fromClientId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupId', full_name='signal.Publication.groupId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupType', full_name='signal.Publication.groupType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='signal.Publication.message', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=1239,
  serialized_end=1327,
)

_GROUPGETCLIENTKEYRESPONSE.fields_by_name['clientKey'].message_type = _GROUPCLIENTKEYOBJECT
_GROUPGETALLCLIENTKEYRESPONSE.fields_by_name['lstClientKey'].message_type = _GROUPCLIENTKEYOBJECT
DESCRIPTOR.message_types_by_name['BaseResponse'] = _BASERESPONSE
DESCRIPTOR.message_types_by_name['PeerRegisterClientKeyRequest'] = _PEERREGISTERCLIENTKEYREQUEST
DESCRIPTOR.message_types_by_name['PeerGetClientKeyRequest'] = _PEERGETCLIENTKEYREQUEST
DESCRIPTOR.message_types_by_name['PeerGetClientKeyResponse'] = _PEERGETCLIENTKEYRESPONSE
DESCRIPTOR.message_types_by_name['GroupRegisterClientKeyRequest'] = _GROUPREGISTERCLIENTKEYREQUEST
DESCRIPTOR.message_types_by_name['GroupClientKeyObject'] = _GROUPCLIENTKEYOBJECT
DESCRIPTOR.message_types_by_name['GroupGetClientKeyRequest'] = _GROUPGETCLIENTKEYREQUEST
DESCRIPTOR.message_types_by_name['GroupGetClientKeyResponse'] = _GROUPGETCLIENTKEYRESPONSE
DESCRIPTOR.message_types_by_name['GroupGetAllClientKeyRequest'] = _GROUPGETALLCLIENTKEYREQUEST
DESCRIPTOR.message_types_by_name['GroupGetAllClientKeyResponse'] = _GROUPGETALLCLIENTKEYRESPONSE
DESCRIPTOR.message_types_by_name['PublishRequest'] = _PUBLISHREQUEST
DESCRIPTOR.message_types_by_name['SubscribeAndListenRequest'] = _SUBSCRIBEANDLISTENREQUEST
DESCRIPTOR.message_types_by_name['Publication'] = _PUBLICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BaseResponse = _reflection.GeneratedProtocolMessageType('BaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _BASERESPONSE,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.BaseResponse)
  })
_sym_db.RegisterMessage(BaseResponse)

PeerRegisterClientKeyRequest = _reflection.GeneratedProtocolMessageType('PeerRegisterClientKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERREGISTERCLIENTKEYREQUEST,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.PeerRegisterClientKeyRequest)
  })
_sym_db.RegisterMessage(PeerRegisterClientKeyRequest)

PeerGetClientKeyRequest = _reflection.GeneratedProtocolMessageType('PeerGetClientKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERGETCLIENTKEYREQUEST,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.PeerGetClientKeyRequest)
  })
_sym_db.RegisterMessage(PeerGetClientKeyRequest)

PeerGetClientKeyResponse = _reflection.GeneratedProtocolMessageType('PeerGetClientKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERGETCLIENTKEYRESPONSE,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.PeerGetClientKeyResponse)
  })
_sym_db.RegisterMessage(PeerGetClientKeyResponse)

GroupRegisterClientKeyRequest = _reflection.GeneratedProtocolMessageType('GroupRegisterClientKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GROUPREGISTERCLIENTKEYREQUEST,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.GroupRegisterClientKeyRequest)
  })
_sym_db.RegisterMessage(GroupRegisterClientKeyRequest)

GroupClientKeyObject = _reflection.GeneratedProtocolMessageType('GroupClientKeyObject', (_message.Message,), {
  'DESCRIPTOR' : _GROUPCLIENTKEYOBJECT,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.GroupClientKeyObject)
  })
_sym_db.RegisterMessage(GroupClientKeyObject)

GroupGetClientKeyRequest = _reflection.GeneratedProtocolMessageType('GroupGetClientKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GROUPGETCLIENTKEYREQUEST,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.GroupGetClientKeyRequest)
  })
_sym_db.RegisterMessage(GroupGetClientKeyRequest)

GroupGetClientKeyResponse = _reflection.GeneratedProtocolMessageType('GroupGetClientKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GROUPGETCLIENTKEYRESPONSE,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.GroupGetClientKeyResponse)
  })
_sym_db.RegisterMessage(GroupGetClientKeyResponse)

GroupGetAllClientKeyRequest = _reflection.GeneratedProtocolMessageType('GroupGetAllClientKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GROUPGETALLCLIENTKEYREQUEST,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.GroupGetAllClientKeyRequest)
  })
_sym_db.RegisterMessage(GroupGetAllClientKeyRequest)

GroupGetAllClientKeyResponse = _reflection.GeneratedProtocolMessageType('GroupGetAllClientKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GROUPGETALLCLIENTKEYRESPONSE,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.GroupGetAllClientKeyResponse)
  })
_sym_db.RegisterMessage(GroupGetAllClientKeyResponse)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHREQUEST,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.PublishRequest)
  })
_sym_db.RegisterMessage(PublishRequest)

SubscribeAndListenRequest = _reflection.GeneratedProtocolMessageType('SubscribeAndListenRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEANDLISTENREQUEST,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.SubscribeAndListenRequest)
  })
_sym_db.RegisterMessage(SubscribeAndListenRequest)

Publication = _reflection.GeneratedProtocolMessageType('Publication', (_message.Message,), {
  'DESCRIPTOR' : _PUBLICATION,
  '__module__' : 'proto.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.Publication)
  })
_sym_db.RegisterMessage(Publication)



_SIGNALKEYDISTRIBUTION = _descriptor.ServiceDescriptor(
  name='SignalKeyDistribution',
  full_name='signal.SignalKeyDistribution',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1330,
  serialized_end=1996,
  methods=[
  _descriptor.MethodDescriptor(
    name='PeerRegisterClientKey',
    full_name='signal.SignalKeyDistribution.PeerRegisterClientKey',
    index=0,
    containing_service=None,
    input_type=_PEERREGISTERCLIENTKEYREQUEST,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PeerGetClientKey',
    full_name='signal.SignalKeyDistribution.PeerGetClientKey',
    index=1,
    containing_service=None,
    input_type=_PEERGETCLIENTKEYREQUEST,
    output_type=_PEERGETCLIENTKEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GroupRegisterClientKey',
    full_name='signal.SignalKeyDistribution.GroupRegisterClientKey',
    index=2,
    containing_service=None,
    input_type=_GROUPREGISTERCLIENTKEYREQUEST,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GroupGetClientKey',
    full_name='signal.SignalKeyDistribution.GroupGetClientKey',
    index=3,
    containing_service=None,
    input_type=_GROUPGETCLIENTKEYREQUEST,
    output_type=_GROUPGETCLIENTKEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GroupGetAllClientKey',
    full_name='signal.SignalKeyDistribution.GroupGetAllClientKey',
    index=4,
    containing_service=None,
    input_type=_GROUPGETALLCLIENTKEYREQUEST,
    output_type=_GROUPGETALLCLIENTKEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='signal.SignalKeyDistribution.Subscribe',
    index=5,
    containing_service=None,
    input_type=_SUBSCRIBEANDLISTENREQUEST,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Listen',
    full_name='signal.SignalKeyDistribution.Listen',
    index=6,
    containing_service=None,
    input_type=_SUBSCRIBEANDLISTENREQUEST,
    output_type=_PUBLICATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Publish',
    full_name='signal.SignalKeyDistribution.Publish',
    index=7,
    containing_service=None,
    input_type=_PUBLISHREQUEST,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIGNALKEYDISTRIBUTION)

DESCRIPTOR.services_by_name['SignalKeyDistribution'] = _SIGNALKEYDISTRIBUTION

# @@protoc_insertion_point(module_scope)
