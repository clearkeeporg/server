# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/group.proto',
  package='group',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12protos/group.proto\x12\x05group\"\xad\x01\n\x15MessageObjectResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\x03\x12\x12\n\ngroup_type\x18\x03 \x01(\t\x12\x16\n\x0e\x66rom_client_id\x18\x04 \x01(\t\x12\x11\n\tclient_id\x18\x05 \x01(\t\x12\x0f\n\x07message\x18\x06 \x01(\x0c\x12\x12\n\ncreated_at\x18\x07 \x01(\x03\x12\x12\n\nupdated_at\x18\x08 \x01(\x03\"2\n\x15\x43lientInGroupResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"\xe1\x02\n\x13GroupObjectResponse\x12\x10\n\x08group_id\x18\x01 \x01(\x03\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x14\n\x0cgroup_avatar\x18\x03 \x01(\t\x12\x12\n\ngroup_type\x18\x04 \x01(\t\x12\x30\n\nlst_client\x18\x05 \x03(\x0b\x32\x1c.group.ClientInGroupResponse\x12\x17\n\x0flast_message_at\x18\x06 \x01(\x03\x12\x32\n\x0clast_message\x18\x07 \x01(\x0b\x32\x1c.group.MessageObjectResponse\x12\x1c\n\x14\x63reated_by_client_id\x18\x08 \x01(\t\x12\x12\n\ncreated_at\x18\t \x01(\x03\x12\x1c\n\x14updated_by_client_id\x18\n \x01(\t\x12\x12\n\nupdated_at\x18\x0b \x01(\x03\x12\x17\n\x0fgroup_rtc_token\x18\x0c \x01(\t\"\x1f\n\x0c\x42\x61seResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"q\n\x12\x43reateGroupRequest\x12\x12\n\ngroup_name\x18\x01 \x01(\t\x12\x12\n\ngroup_type\x18\x02 \x01(\t\x12\x1c\n\x14\x63reated_by_client_id\x18\x03 \x01(\t\x12\x15\n\rlst_client_id\x18\x04 \x03(\t\"n\n\x12UpdateGroupRequest\x12\x10\n\x08group_id\x18\x01 \x01(\x03\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x14\n\x0cgroup_avatar\x18\x03 \x01(\t\x12\x1c\n\x14updated_by_client_id\x18\x04 \x01(\t\"#\n\x0fGetGroupRequest\x12\x10\n\x08group_id\x18\x01 \x01(\x03\"+\n\x16GetJoinedGroupsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\"H\n\x17GetJoinedGroupsResponse\x12-\n\tlst_group\x18\x01 \x03(\x0b\x32\x1a.group.GroupObjectResponse\"&\n\x13SearchGroupsRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"E\n\x14SearchGroupsResponse\x12-\n\tlst_group\x18\x01 \x03(\x0b\x32\x1a.group.GroupObjectResponse\"S\n\x14InviteToGroupRequest\x12\x16\n\x0e\x66rom_client_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\x10\n\x08group_id\x18\x03 \x01(\x03\"7\n\x10JoinGroupRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\x03\x32\xba\x03\n\x05Group\x12G\n\x0c\x63reate_group\x12\x19.group.CreateGroupRequest\x1a\x1a.group.GroupObjectResponse\"\x00\x12\x41\n\tget_group\x12\x16.group.GetGroupRequest\x1a\x1a.group.GroupObjectResponse\"\x00\x12J\n\rsearch_groups\x12\x1a.group.SearchGroupsRequest\x1a\x1b.group.SearchGroupsResponse\"\x00\x12T\n\x11get_joined_groups\x12\x1d.group.GetJoinedGroupsRequest\x1a\x1e.group.GetJoinedGroupsResponse\"\x00\x12\x45\n\x0finvite_to_group\x12\x1b.group.InviteToGroupRequest\x1a\x13.group.BaseResponse\"\x00\x12<\n\njoin_group\x12\x17.group.JoinGroupRequest\x1a\x13.group.BaseResponse\"\x00\x62\x06proto3'
)




_MESSAGEOBJECTRESPONSE = _descriptor.Descriptor(
  name='MessageObjectResponse',
  full_name='group.MessageObjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='group.MessageObjectResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.MessageObjectResponse.group_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_type', full_name='group.MessageObjectResponse.group_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_client_id', full_name='group.MessageObjectResponse.from_client_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='group.MessageObjectResponse.client_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='group.MessageObjectResponse.message', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='group.MessageObjectResponse.created_at', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='group.MessageObjectResponse.updated_at', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=203,
)


_CLIENTINGROUPRESPONSE = _descriptor.Descriptor(
  name='ClientInGroupResponse',
  full_name='group.ClientInGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='group.ClientInGroupResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='group.ClientInGroupResponse.email', index=1,
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
  serialized_start=205,
  serialized_end=255,
)


_GROUPOBJECTRESPONSE = _descriptor.Descriptor(
  name='GroupObjectResponse',
  full_name='group.GroupObjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.GroupObjectResponse.group_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='group.GroupObjectResponse.group_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_avatar', full_name='group.GroupObjectResponse.group_avatar', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_type', full_name='group.GroupObjectResponse.group_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lst_client', full_name='group.GroupObjectResponse.lst_client', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_message_at', full_name='group.GroupObjectResponse.last_message_at', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_message', full_name='group.GroupObjectResponse.last_message', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_by_client_id', full_name='group.GroupObjectResponse.created_by_client_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='group.GroupObjectResponse.created_at', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_by_client_id', full_name='group.GroupObjectResponse.updated_by_client_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='group.GroupObjectResponse.updated_at', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_rtc_token', full_name='group.GroupObjectResponse.group_rtc_token', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=258,
  serialized_end=611,
)


_BASERESPONSE = _descriptor.Descriptor(
  name='BaseResponse',
  full_name='group.BaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='group.BaseResponse.success', index=0,
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
  serialized_start=613,
  serialized_end=644,
)


_CREATEGROUPREQUEST = _descriptor.Descriptor(
  name='CreateGroupRequest',
  full_name='group.CreateGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_name', full_name='group.CreateGroupRequest.group_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_type', full_name='group.CreateGroupRequest.group_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_by_client_id', full_name='group.CreateGroupRequest.created_by_client_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lst_client_id', full_name='group.CreateGroupRequest.lst_client_id', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=646,
  serialized_end=759,
)


_UPDATEGROUPREQUEST = _descriptor.Descriptor(
  name='UpdateGroupRequest',
  full_name='group.UpdateGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.UpdateGroupRequest.group_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='group.UpdateGroupRequest.group_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_avatar', full_name='group.UpdateGroupRequest.group_avatar', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_by_client_id', full_name='group.UpdateGroupRequest.updated_by_client_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=761,
  serialized_end=871,
)


_GETGROUPREQUEST = _descriptor.Descriptor(
  name='GetGroupRequest',
  full_name='group.GetGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.GetGroupRequest.group_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=873,
  serialized_end=908,
)


_GETJOINEDGROUPSREQUEST = _descriptor.Descriptor(
  name='GetJoinedGroupsRequest',
  full_name='group.GetJoinedGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='group.GetJoinedGroupsRequest.client_id', index=0,
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
  serialized_start=910,
  serialized_end=953,
)


_GETJOINEDGROUPSRESPONSE = _descriptor.Descriptor(
  name='GetJoinedGroupsResponse',
  full_name='group.GetJoinedGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lst_group', full_name='group.GetJoinedGroupsResponse.lst_group', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=955,
  serialized_end=1027,
)


_SEARCHGROUPSREQUEST = _descriptor.Descriptor(
  name='SearchGroupsRequest',
  full_name='group.SearchGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword', full_name='group.SearchGroupsRequest.keyword', index=0,
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
  serialized_start=1029,
  serialized_end=1067,
)


_SEARCHGROUPSRESPONSE = _descriptor.Descriptor(
  name='SearchGroupsResponse',
  full_name='group.SearchGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lst_group', full_name='group.SearchGroupsResponse.lst_group', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1069,
  serialized_end=1138,
)


_INVITETOGROUPREQUEST = _descriptor.Descriptor(
  name='InviteToGroupRequest',
  full_name='group.InviteToGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_client_id', full_name='group.InviteToGroupRequest.from_client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='group.InviteToGroupRequest.client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.InviteToGroupRequest.group_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1140,
  serialized_end=1223,
)


_JOINGROUPREQUEST = _descriptor.Descriptor(
  name='JoinGroupRequest',
  full_name='group.JoinGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='group.JoinGroupRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.JoinGroupRequest.group_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1225,
  serialized_end=1280,
)

_GROUPOBJECTRESPONSE.fields_by_name['lst_client'].message_type = _CLIENTINGROUPRESPONSE
_GROUPOBJECTRESPONSE.fields_by_name['last_message'].message_type = _MESSAGEOBJECTRESPONSE
_GETJOINEDGROUPSRESPONSE.fields_by_name['lst_group'].message_type = _GROUPOBJECTRESPONSE
_SEARCHGROUPSRESPONSE.fields_by_name['lst_group'].message_type = _GROUPOBJECTRESPONSE
DESCRIPTOR.message_types_by_name['MessageObjectResponse'] = _MESSAGEOBJECTRESPONSE
DESCRIPTOR.message_types_by_name['ClientInGroupResponse'] = _CLIENTINGROUPRESPONSE
DESCRIPTOR.message_types_by_name['GroupObjectResponse'] = _GROUPOBJECTRESPONSE
DESCRIPTOR.message_types_by_name['BaseResponse'] = _BASERESPONSE
DESCRIPTOR.message_types_by_name['CreateGroupRequest'] = _CREATEGROUPREQUEST
DESCRIPTOR.message_types_by_name['UpdateGroupRequest'] = _UPDATEGROUPREQUEST
DESCRIPTOR.message_types_by_name['GetGroupRequest'] = _GETGROUPREQUEST
DESCRIPTOR.message_types_by_name['GetJoinedGroupsRequest'] = _GETJOINEDGROUPSREQUEST
DESCRIPTOR.message_types_by_name['GetJoinedGroupsResponse'] = _GETJOINEDGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['SearchGroupsRequest'] = _SEARCHGROUPSREQUEST
DESCRIPTOR.message_types_by_name['SearchGroupsResponse'] = _SEARCHGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['InviteToGroupRequest'] = _INVITETOGROUPREQUEST
DESCRIPTOR.message_types_by_name['JoinGroupRequest'] = _JOINGROUPREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageObjectResponse = _reflection.GeneratedProtocolMessageType('MessageObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEOBJECTRESPONSE,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.MessageObjectResponse)
  })
_sym_db.RegisterMessage(MessageObjectResponse)

ClientInGroupResponse = _reflection.GeneratedProtocolMessageType('ClientInGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTINGROUPRESPONSE,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.ClientInGroupResponse)
  })
_sym_db.RegisterMessage(ClientInGroupResponse)

GroupObjectResponse = _reflection.GeneratedProtocolMessageType('GroupObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _GROUPOBJECTRESPONSE,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.GroupObjectResponse)
  })
_sym_db.RegisterMessage(GroupObjectResponse)

BaseResponse = _reflection.GeneratedProtocolMessageType('BaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _BASERESPONSE,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.BaseResponse)
  })
_sym_db.RegisterMessage(BaseResponse)

CreateGroupRequest = _reflection.GeneratedProtocolMessageType('CreateGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGROUPREQUEST,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.CreateGroupRequest)
  })
_sym_db.RegisterMessage(CreateGroupRequest)

UpdateGroupRequest = _reflection.GeneratedProtocolMessageType('UpdateGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGROUPREQUEST,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.UpdateGroupRequest)
  })
_sym_db.RegisterMessage(UpdateGroupRequest)

GetGroupRequest = _reflection.GeneratedProtocolMessageType('GetGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGROUPREQUEST,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.GetGroupRequest)
  })
_sym_db.RegisterMessage(GetGroupRequest)

GetJoinedGroupsRequest = _reflection.GeneratedProtocolMessageType('GetJoinedGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOINEDGROUPSREQUEST,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.GetJoinedGroupsRequest)
  })
_sym_db.RegisterMessage(GetJoinedGroupsRequest)

GetJoinedGroupsResponse = _reflection.GeneratedProtocolMessageType('GetJoinedGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETJOINEDGROUPSRESPONSE,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.GetJoinedGroupsResponse)
  })
_sym_db.RegisterMessage(GetJoinedGroupsResponse)

SearchGroupsRequest = _reflection.GeneratedProtocolMessageType('SearchGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHGROUPSREQUEST,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.SearchGroupsRequest)
  })
_sym_db.RegisterMessage(SearchGroupsRequest)

SearchGroupsResponse = _reflection.GeneratedProtocolMessageType('SearchGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHGROUPSRESPONSE,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.SearchGroupsResponse)
  })
_sym_db.RegisterMessage(SearchGroupsResponse)

InviteToGroupRequest = _reflection.GeneratedProtocolMessageType('InviteToGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVITETOGROUPREQUEST,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.InviteToGroupRequest)
  })
_sym_db.RegisterMessage(InviteToGroupRequest)

JoinGroupRequest = _reflection.GeneratedProtocolMessageType('JoinGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOINGROUPREQUEST,
  '__module__' : 'protos.group_pb2'
  # @@protoc_insertion_point(class_scope:group.JoinGroupRequest)
  })
_sym_db.RegisterMessage(JoinGroupRequest)



_GROUP = _descriptor.ServiceDescriptor(
  name='Group',
  full_name='group.Group',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1283,
  serialized_end=1725,
  methods=[
  _descriptor.MethodDescriptor(
    name='create_group',
    full_name='group.Group.create_group',
    index=0,
    containing_service=None,
    input_type=_CREATEGROUPREQUEST,
    output_type=_GROUPOBJECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_group',
    full_name='group.Group.get_group',
    index=1,
    containing_service=None,
    input_type=_GETGROUPREQUEST,
    output_type=_GROUPOBJECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='search_groups',
    full_name='group.Group.search_groups',
    index=2,
    containing_service=None,
    input_type=_SEARCHGROUPSREQUEST,
    output_type=_SEARCHGROUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_joined_groups',
    full_name='group.Group.get_joined_groups',
    index=3,
    containing_service=None,
    input_type=_GETJOINEDGROUPSREQUEST,
    output_type=_GETJOINEDGROUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='invite_to_group',
    full_name='group.Group.invite_to_group',
    index=4,
    containing_service=None,
    input_type=_INVITETOGROUPREQUEST,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='join_group',
    full_name='group.Group.join_group',
    index=5,
    containing_service=None,
    input_type=_JOINGROUPREQUEST,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GROUP)

DESCRIPTOR.services_by_name['Group'] = _GROUP

# @@protoc_insertion_point(module_scope)
