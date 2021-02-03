# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/user.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11protos/user.proto\x12\x04user\")\n\x08\x45rrorRes\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\"?\n\x0c\x42\x61seResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1e\n\x06\x65rrors\x18\x02 \x01(\x0b\x32\x0e.user.ErrorRes\"m\n\x13UserProfileResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x12\n\nfirst_name\x18\x04 \x01(\t\x12\x11\n\tlast_name\x18\x05 \x01(\t\"\x07\n\x05\x45mpty\"M\n\x14UpdateProfileRequest\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t\"C\n\x15\x43hangePasswordRequest\x12\x14\n\x0cold_password\x18\x01 \x01(\t\x12\x14\n\x0cnew_password\x18\x02 \x01(\t\"D\n\x10UserInfoResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\"3\n\x0eGetUserRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\"$\n\x11SearchUserRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\">\n\x12SearchUserResponse\x12(\n\x08lst_user\x18\x01 \x03(\x0b\x32\x16.user.UserInfoResponse\"<\n\x10GetUsersResponse\x12(\n\x08lst_user\x18\x01 \x03(\x0b\x32\x16.user.UserInfoResponse2\x82\x03\n\x04User\x12\x37\n\x0bget_profile\x12\x0b.user.Empty\x1a\x19.user.UserProfileResponse\"\x00\x12\x42\n\x0eupdate_profile\x12\x1a.user.UpdateProfileRequest\x1a\x12.user.BaseResponse\"\x00\x12\x44\n\x0f\x63hange_password\x12\x1b.user.ChangePasswordRequest\x1a\x12.user.BaseResponse\"\x00\x12?\n\rget_user_info\x12\x14.user.GetUserRequest\x1a\x16.user.UserInfoResponse\"\x00\x12\x42\n\x0bsearch_user\x12\x17.user.SearchUserRequest\x1a\x18.user.SearchUserResponse\"\x00\x12\x32\n\tget_users\x12\x0b.user.Empty\x1a\x16.user.GetUsersResponse\"\x00\x62\x06proto3'
)




_ERRORRES = _descriptor.Descriptor(
  name='ErrorRes',
  full_name='user.ErrorRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user.ErrorRes.code', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='user.ErrorRes.message', index=1,
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
  serialized_start=27,
  serialized_end=68,
)


_BASERESPONSE = _descriptor.Descriptor(
  name='BaseResponse',
  full_name='user.BaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='user.BaseResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='user.BaseResponse.errors', index=1,
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
  serialized_start=70,
  serialized_end=133,
)


_USERPROFILERESPONSE = _descriptor.Descriptor(
  name='UserProfileResponse',
  full_name='user.UserProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.UserProfileResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='user.UserProfileResponse.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='user.UserProfileResponse.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='user.UserProfileResponse.first_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='user.UserProfileResponse.last_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=135,
  serialized_end=244,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='user.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=246,
  serialized_end=253,
)


_UPDATEPROFILEREQUEST = _descriptor.Descriptor(
  name='UpdateProfileRequest',
  full_name='user.UpdateProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='user.UpdateProfileRequest.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='user.UpdateProfileRequest.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='user.UpdateProfileRequest.avatar', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=255,
  serialized_end=332,
)


_CHANGEPASSWORDREQUEST = _descriptor.Descriptor(
  name='ChangePasswordRequest',
  full_name='user.ChangePasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='old_password', full_name='user.ChangePasswordRequest.old_password', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_password', full_name='user.ChangePasswordRequest.new_password', index=1,
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
  serialized_start=334,
  serialized_end=401,
)


_USERINFORESPONSE = _descriptor.Descriptor(
  name='UserInfoResponse',
  full_name='user.UserInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.UserInfoResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='user.UserInfoResponse.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='user.UserInfoResponse.domain', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=403,
  serialized_end=471,
)


_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='user.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='user.GetUserRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='user.GetUserRequest.domain', index=1,
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
  serialized_start=473,
  serialized_end=524,
)


_SEARCHUSERREQUEST = _descriptor.Descriptor(
  name='SearchUserRequest',
  full_name='user.SearchUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword', full_name='user.SearchUserRequest.keyword', index=0,
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
  serialized_start=526,
  serialized_end=562,
)


_SEARCHUSERRESPONSE = _descriptor.Descriptor(
  name='SearchUserResponse',
  full_name='user.SearchUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lst_user', full_name='user.SearchUserResponse.lst_user', index=0,
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
  serialized_start=564,
  serialized_end=626,
)


_GETUSERSRESPONSE = _descriptor.Descriptor(
  name='GetUsersResponse',
  full_name='user.GetUsersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lst_user', full_name='user.GetUsersResponse.lst_user', index=0,
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
  serialized_start=628,
  serialized_end=688,
)

_BASERESPONSE.fields_by_name['errors'].message_type = _ERRORRES
_SEARCHUSERRESPONSE.fields_by_name['lst_user'].message_type = _USERINFORESPONSE
_GETUSERSRESPONSE.fields_by_name['lst_user'].message_type = _USERINFORESPONSE
DESCRIPTOR.message_types_by_name['ErrorRes'] = _ERRORRES
DESCRIPTOR.message_types_by_name['BaseResponse'] = _BASERESPONSE
DESCRIPTOR.message_types_by_name['UserProfileResponse'] = _USERPROFILERESPONSE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['UpdateProfileRequest'] = _UPDATEPROFILEREQUEST
DESCRIPTOR.message_types_by_name['ChangePasswordRequest'] = _CHANGEPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['UserInfoResponse'] = _USERINFORESPONSE
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['SearchUserRequest'] = _SEARCHUSERREQUEST
DESCRIPTOR.message_types_by_name['SearchUserResponse'] = _SEARCHUSERRESPONSE
DESCRIPTOR.message_types_by_name['GetUsersResponse'] = _GETUSERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorRes = _reflection.GeneratedProtocolMessageType('ErrorRes', (_message.Message,), {
  'DESCRIPTOR' : _ERRORRES,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.ErrorRes)
  })
_sym_db.RegisterMessage(ErrorRes)

BaseResponse = _reflection.GeneratedProtocolMessageType('BaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _BASERESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.BaseResponse)
  })
_sym_db.RegisterMessage(BaseResponse)

UserProfileResponse = _reflection.GeneratedProtocolMessageType('UserProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERPROFILERESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserProfileResponse)
  })
_sym_db.RegisterMessage(UserProfileResponse)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.Empty)
  })
_sym_db.RegisterMessage(Empty)

UpdateProfileRequest = _reflection.GeneratedProtocolMessageType('UpdateProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROFILEREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.UpdateProfileRequest)
  })
_sym_db.RegisterMessage(UpdateProfileRequest)

ChangePasswordRequest = _reflection.GeneratedProtocolMessageType('ChangePasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEPASSWORDREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.ChangePasswordRequest)
  })
_sym_db.RegisterMessage(ChangePasswordRequest)

UserInfoResponse = _reflection.GeneratedProtocolMessageType('UserInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERINFORESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserInfoResponse)
  })
_sym_db.RegisterMessage(UserInfoResponse)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

SearchUserRequest = _reflection.GeneratedProtocolMessageType('SearchUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHUSERREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.SearchUserRequest)
  })
_sym_db.RegisterMessage(SearchUserRequest)

SearchUserResponse = _reflection.GeneratedProtocolMessageType('SearchUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHUSERRESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.SearchUserResponse)
  })
_sym_db.RegisterMessage(SearchUserResponse)

GetUsersResponse = _reflection.GeneratedProtocolMessageType('GetUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERSRESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.GetUsersResponse)
  })
_sym_db.RegisterMessage(GetUsersResponse)



_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='user.User',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=691,
  serialized_end=1077,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_profile',
    full_name='user.User.get_profile',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_USERPROFILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update_profile',
    full_name='user.User.update_profile',
    index=1,
    containing_service=None,
    input_type=_UPDATEPROFILEREQUEST,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='change_password',
    full_name='user.User.change_password',
    index=2,
    containing_service=None,
    input_type=_CHANGEPASSWORDREQUEST,
    output_type=_BASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_user_info',
    full_name='user.User.get_user_info',
    index=3,
    containing_service=None,
    input_type=_GETUSERREQUEST,
    output_type=_USERINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='search_user',
    full_name='user.User.search_user',
    index=4,
    containing_service=None,
    input_type=_SEARCHUSERREQUEST,
    output_type=_SEARCHUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_users',
    full_name='user.User.get_users',
    index=5,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_GETUSERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)
