# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/user.proto\x12\x04user\"\x1d\n\x0c\x42\x61seResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"l\n\x13UserProfileResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x05 \x01(\t\"\x07\n\x05\x45mpty\"n\n\x14UpdateProfileRequest\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\x1a\n\x12\x63lear_phone_number\x18\x04 \x01(\x08\"1\n\x18RequestChangePasswordReq\x12\x15\n\rclient_public\x18\x01 \x01(\t\"D\n\x18RequestChangePasswordRes\x12\x0c\n\x04salt\x18\x01 \x01(\t\x12\x1a\n\x12public_challenge_b\x18\x02 \x01(\t\"\xab\x01\n\x15\x43hangePasswordRequest\x12\x15\n\rclient_public\x18\x01 \x01(\t\x12 \n\x18\x63lient_session_key_proof\x18\x03 \x01(\t\x12\x15\n\rhash_password\x18\x04 \x01(\t\x12\x0c\n\x04salt\x18\x05 \x01(\t\x12\x14\n\x0civ_parameter\x18\x06 \x01(\t\x12\x1e\n\x16identity_key_encrypted\x18\x07 \x01(\t\"^\n\x10UserInfoResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x18\n\x10workspace_domain\x18\x03 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x01(\t\"=\n\x0eGetUserRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x18\n\x10workspace_domain\x18\x02 \x01(\t\"$\n\x11SearchUserRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\">\n\x12SearchUserResponse\x12(\n\x08lst_user\x18\x01 \x03(\x0b\x32\x16.user.UserInfoResponse\",\n\x16\x46indUserByEmailRequest\x12\x12\n\nemail_hash\x18\x01 \x01(\t\"C\n\x17\x46indUserByEmailResponse\x12(\n\x08lst_user\x18\x01 \x03(\x0b\x32\x16.user.UserInfoResponse\"<\n\x10GetUsersResponse\x12(\n\x08lst_user\x18\x01 \x03(\x0b\x32\x16.user.UserInfoResponse\"&\n\x14SetUserStatusRequest\x12\x0e\n\x06status\x18\x01 \x01(\t\"\r\n\x0bPingRequest\"b\n\x17GetClientsStatusRequest\x12+\n\nlst_client\x18\x01 \x03(\x0b\x32\x17.user.MemberInfoRequest\x12\x1a\n\x12should_get_profile\x18\x02 \x01(\x08\"@\n\x11MemberInfoRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x18\n\x10workspace_domain\x18\x02 \x01(\t\"C\n\x18GetClientsStatusResponse\x12\'\n\nlst_client\x18\x01 \x03(\x0b\x32\x13.user.MemberInfoRes\"\x88\x01\n\rMemberInfoRes\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x18\n\x10workspace_domain\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x05 \x01(\t\x12\x14\n\x0cphone_number\x18\x06 \x01(\t\"i\n\x13UploadAvatarRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x19\n\x11\x66ile_content_type\x18\x02 \x01(\t\x12\x11\n\tfile_data\x18\x03 \x01(\x0c\x12\x11\n\tfile_hash\x18\x04 \x01(\t\"(\n\x14UploadAvatarResponse\x12\x10\n\x08\x66ile_url\x18\x01 \x01(\t\"D\n\x0fMfaBaseResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x11\n\tnext_step\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"5\n\x10MfaStateResponse\x12\x12\n\nmfa_enable\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\x14\n\x12MfaGetStateRequest\"\x19\n\x17MfaChangingStateRequest\"0\n\x17MfaAuthChallengeRequest\x12\x15\n\rclient_public\x18\x01 \x01(\t\"D\n\x18MfaAuthChallengeResponse\x12\x0c\n\x04salt\x18\x01 \x01(\t\x12\x1a\n\x12public_challenge_b\x18\x02 \x01(\t\"U\n\x1aMfaValidatePasswordRequest\x12\x15\n\rclient_public\x18\x01 \x01(\t\x12 \n\x18\x63lient_session_key_proof\x18\x02 \x01(\t\"$\n\x15MfaValidateOtpRequest\x12\x0b\n\x03otp\x18\x01 \x01(\t\"\x15\n\x13MfaResendOtpRequest\"J\n!WorkspaceUpdateDisplayNameRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t2\xd4\x0c\n\x04User\x12\x37\n\x0bget_profile\x12\x0b.user.Empty\x1a\x19.user.UserProfileResponse\"\x00\x12\x42\n\x0eupdate_profile\x12\x1a.user.UpdateProfileRequest\x1a\x12.user.BaseResponse\"\x00\x12H\n\rupload_avatar\x12\x19.user.UploadAvatarRequest\x1a\x1a.user.UploadAvatarResponse\"\x00\x12[\n\x17request_change_password\x12\x1e.user.RequestChangePasswordReq\x1a\x1e.user.RequestChangePasswordRes\"\x00\x12\x44\n\x0f\x63hange_password\x12\x1b.user.ChangePasswordRequest\x1a\x12.user.BaseResponse\"\x00\x12\x41\n\rupdate_status\x12\x1a.user.SetUserStatusRequest\x1a\x12.user.BaseResponse\"\x00\x12\x37\n\x0cping_request\x12\x11.user.PingRequest\x1a\x12.user.BaseResponse\"\x00\x12U\n\x12get_clients_status\x12\x1d.user.GetClientsStatusRequest\x1a\x1e.user.GetClientsStatusResponse\"\x00\x12\x33\n\x0e\x64\x65lete_account\x12\x0b.user.Empty\x1a\x12.user.BaseResponse\"\x00\x12?\n\rget_user_info\x12\x14.user.GetUserRequest\x1a\x16.user.UserInfoResponse\"\x00\x12\x42\n\x0bsearch_user\x12\x17.user.SearchUserRequest\x1a\x18.user.SearchUserResponse\"\x00\x12\x32\n\tget_users\x12\x0b.user.Empty\x1a\x16.user.GetUsersResponse\"\x00\x12S\n\x12\x66ind_user_by_email\x12\x1c.user.FindUserByEmailRequest\x1a\x1d.user.FindUserByEmailResponse\"\x00\x12_\n%find_user_detail_info_from_email_hash\x12\x1c.user.FindUserByEmailRequest\x1a\x16.user.UserInfoResponse\"\x00\x12\x43\n\rget_mfa_state\x12\x18.user.MfaGetStateRequest\x1a\x16.user.MfaStateResponse\"\x00\x12\x44\n\nenable_mfa\x12\x1d.user.MfaChangingStateRequest\x1a\x15.user.MfaBaseResponse\"\x00\x12\x45\n\x0b\x64isable_mfa\x12\x1d.user.MfaChangingStateRequest\x1a\x15.user.MfaBaseResponse\"\x00\x12U\n\x12mfa_auth_challenge\x12\x1d.user.MfaAuthChallengeRequest\x1a\x1e.user.MfaAuthChallengeResponse\"\x00\x12R\n\x15mfa_validate_password\x12 .user.MfaValidatePasswordRequest\x1a\x15.user.MfaBaseResponse\"\x00\x12H\n\x10mfa_validate_otp\x12\x1b.user.MfaValidateOtpRequest\x1a\x15.user.MfaBaseResponse\"\x00\x12\x44\n\x0emfa_resend_otp\x12\x19.user.MfaResendOtpRequest\x1a\x15.user.MfaBaseResponse\"\x00\x12^\n\x1dworkspace_update_display_name\x12\'.user.WorkspaceUpdateDisplayNameRequest\x1a\x12.user.BaseResponse\"\x00\x62\x06proto3')



_BASERESPONSE = DESCRIPTOR.message_types_by_name['BaseResponse']
_USERPROFILERESPONSE = DESCRIPTOR.message_types_by_name['UserProfileResponse']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_UPDATEPROFILEREQUEST = DESCRIPTOR.message_types_by_name['UpdateProfileRequest']
_REQUESTCHANGEPASSWORDREQ = DESCRIPTOR.message_types_by_name['RequestChangePasswordReq']
_REQUESTCHANGEPASSWORDRES = DESCRIPTOR.message_types_by_name['RequestChangePasswordRes']
_CHANGEPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['ChangePasswordRequest']
_USERINFORESPONSE = DESCRIPTOR.message_types_by_name['UserInfoResponse']
_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_SEARCHUSERREQUEST = DESCRIPTOR.message_types_by_name['SearchUserRequest']
_SEARCHUSERRESPONSE = DESCRIPTOR.message_types_by_name['SearchUserResponse']
_FINDUSERBYEMAILREQUEST = DESCRIPTOR.message_types_by_name['FindUserByEmailRequest']
_FINDUSERBYEMAILRESPONSE = DESCRIPTOR.message_types_by_name['FindUserByEmailResponse']
_GETUSERSRESPONSE = DESCRIPTOR.message_types_by_name['GetUsersResponse']
_SETUSERSTATUSREQUEST = DESCRIPTOR.message_types_by_name['SetUserStatusRequest']
_PINGREQUEST = DESCRIPTOR.message_types_by_name['PingRequest']
_GETCLIENTSSTATUSREQUEST = DESCRIPTOR.message_types_by_name['GetClientsStatusRequest']
_MEMBERINFOREQUEST = DESCRIPTOR.message_types_by_name['MemberInfoRequest']
_GETCLIENTSSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['GetClientsStatusResponse']
_MEMBERINFORES = DESCRIPTOR.message_types_by_name['MemberInfoRes']
_UPLOADAVATARREQUEST = DESCRIPTOR.message_types_by_name['UploadAvatarRequest']
_UPLOADAVATARRESPONSE = DESCRIPTOR.message_types_by_name['UploadAvatarResponse']
_MFABASERESPONSE = DESCRIPTOR.message_types_by_name['MfaBaseResponse']
_MFASTATERESPONSE = DESCRIPTOR.message_types_by_name['MfaStateResponse']
_MFAGETSTATEREQUEST = DESCRIPTOR.message_types_by_name['MfaGetStateRequest']
_MFACHANGINGSTATEREQUEST = DESCRIPTOR.message_types_by_name['MfaChangingStateRequest']
_MFAAUTHCHALLENGEREQUEST = DESCRIPTOR.message_types_by_name['MfaAuthChallengeRequest']
_MFAAUTHCHALLENGERESPONSE = DESCRIPTOR.message_types_by_name['MfaAuthChallengeResponse']
_MFAVALIDATEPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['MfaValidatePasswordRequest']
_MFAVALIDATEOTPREQUEST = DESCRIPTOR.message_types_by_name['MfaValidateOtpRequest']
_MFARESENDOTPREQUEST = DESCRIPTOR.message_types_by_name['MfaResendOtpRequest']
_WORKSPACEUPDATEDISPLAYNAMEREQUEST = DESCRIPTOR.message_types_by_name['WorkspaceUpdateDisplayNameRequest']
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

RequestChangePasswordReq = _reflection.GeneratedProtocolMessageType('RequestChangePasswordReq', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCHANGEPASSWORDREQ,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.RequestChangePasswordReq)
  })
_sym_db.RegisterMessage(RequestChangePasswordReq)

RequestChangePasswordRes = _reflection.GeneratedProtocolMessageType('RequestChangePasswordRes', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCHANGEPASSWORDRES,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.RequestChangePasswordRes)
  })
_sym_db.RegisterMessage(RequestChangePasswordRes)

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

FindUserByEmailRequest = _reflection.GeneratedProtocolMessageType('FindUserByEmailRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERBYEMAILREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.FindUserByEmailRequest)
  })
_sym_db.RegisterMessage(FindUserByEmailRequest)

FindUserByEmailResponse = _reflection.GeneratedProtocolMessageType('FindUserByEmailResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERBYEMAILRESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.FindUserByEmailResponse)
  })
_sym_db.RegisterMessage(FindUserByEmailResponse)

GetUsersResponse = _reflection.GeneratedProtocolMessageType('GetUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERSRESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.GetUsersResponse)
  })
_sym_db.RegisterMessage(GetUsersResponse)

SetUserStatusRequest = _reflection.GeneratedProtocolMessageType('SetUserStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETUSERSTATUSREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.SetUserStatusRequest)
  })
_sym_db.RegisterMessage(SetUserStatusRequest)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

GetClientsStatusRequest = _reflection.GeneratedProtocolMessageType('GetClientsStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTSSTATUSREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.GetClientsStatusRequest)
  })
_sym_db.RegisterMessage(GetClientsStatusRequest)

MemberInfoRequest = _reflection.GeneratedProtocolMessageType('MemberInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _MEMBERINFOREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MemberInfoRequest)
  })
_sym_db.RegisterMessage(MemberInfoRequest)

GetClientsStatusResponse = _reflection.GeneratedProtocolMessageType('GetClientsStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTSSTATUSRESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.GetClientsStatusResponse)
  })
_sym_db.RegisterMessage(GetClientsStatusResponse)

MemberInfoRes = _reflection.GeneratedProtocolMessageType('MemberInfoRes', (_message.Message,), {
  'DESCRIPTOR' : _MEMBERINFORES,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MemberInfoRes)
  })
_sym_db.RegisterMessage(MemberInfoRes)

UploadAvatarRequest = _reflection.GeneratedProtocolMessageType('UploadAvatarRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADAVATARREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.UploadAvatarRequest)
  })
_sym_db.RegisterMessage(UploadAvatarRequest)

UploadAvatarResponse = _reflection.GeneratedProtocolMessageType('UploadAvatarResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADAVATARRESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.UploadAvatarResponse)
  })
_sym_db.RegisterMessage(UploadAvatarResponse)

MfaBaseResponse = _reflection.GeneratedProtocolMessageType('MfaBaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _MFABASERESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaBaseResponse)
  })
_sym_db.RegisterMessage(MfaBaseResponse)

MfaStateResponse = _reflection.GeneratedProtocolMessageType('MfaStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _MFASTATERESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaStateResponse)
  })
_sym_db.RegisterMessage(MfaStateResponse)

MfaGetStateRequest = _reflection.GeneratedProtocolMessageType('MfaGetStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _MFAGETSTATEREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaGetStateRequest)
  })
_sym_db.RegisterMessage(MfaGetStateRequest)

MfaChangingStateRequest = _reflection.GeneratedProtocolMessageType('MfaChangingStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _MFACHANGINGSTATEREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaChangingStateRequest)
  })
_sym_db.RegisterMessage(MfaChangingStateRequest)

MfaAuthChallengeRequest = _reflection.GeneratedProtocolMessageType('MfaAuthChallengeRequest', (_message.Message,), {
  'DESCRIPTOR' : _MFAAUTHCHALLENGEREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaAuthChallengeRequest)
  })
_sym_db.RegisterMessage(MfaAuthChallengeRequest)

MfaAuthChallengeResponse = _reflection.GeneratedProtocolMessageType('MfaAuthChallengeResponse', (_message.Message,), {
  'DESCRIPTOR' : _MFAAUTHCHALLENGERESPONSE,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaAuthChallengeResponse)
  })
_sym_db.RegisterMessage(MfaAuthChallengeResponse)

MfaValidatePasswordRequest = _reflection.GeneratedProtocolMessageType('MfaValidatePasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _MFAVALIDATEPASSWORDREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaValidatePasswordRequest)
  })
_sym_db.RegisterMessage(MfaValidatePasswordRequest)

MfaValidateOtpRequest = _reflection.GeneratedProtocolMessageType('MfaValidateOtpRequest', (_message.Message,), {
  'DESCRIPTOR' : _MFAVALIDATEOTPREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaValidateOtpRequest)
  })
_sym_db.RegisterMessage(MfaValidateOtpRequest)

MfaResendOtpRequest = _reflection.GeneratedProtocolMessageType('MfaResendOtpRequest', (_message.Message,), {
  'DESCRIPTOR' : _MFARESENDOTPREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.MfaResendOtpRequest)
  })
_sym_db.RegisterMessage(MfaResendOtpRequest)

WorkspaceUpdateDisplayNameRequest = _reflection.GeneratedProtocolMessageType('WorkspaceUpdateDisplayNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKSPACEUPDATEDISPLAYNAMEREQUEST,
  '__module__' : 'protos.user_pb2'
  # @@protoc_insertion_point(class_scope:user.WorkspaceUpdateDisplayNameRequest)
  })
_sym_db.RegisterMessage(WorkspaceUpdateDisplayNameRequest)

_USER = DESCRIPTOR.services_by_name['User']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BASERESPONSE._serialized_start=27
  _BASERESPONSE._serialized_end=56
  _USERPROFILERESPONSE._serialized_start=58
  _USERPROFILERESPONSE._serialized_end=166
  _EMPTY._serialized_start=168
  _EMPTY._serialized_end=175
  _UPDATEPROFILEREQUEST._serialized_start=177
  _UPDATEPROFILEREQUEST._serialized_end=287
  _REQUESTCHANGEPASSWORDREQ._serialized_start=289
  _REQUESTCHANGEPASSWORDREQ._serialized_end=338
  _REQUESTCHANGEPASSWORDRES._serialized_start=340
  _REQUESTCHANGEPASSWORDRES._serialized_end=408
  _CHANGEPASSWORDREQUEST._serialized_start=411
  _CHANGEPASSWORDREQUEST._serialized_end=582
  _USERINFORESPONSE._serialized_start=584
  _USERINFORESPONSE._serialized_end=678
  _GETUSERREQUEST._serialized_start=680
  _GETUSERREQUEST._serialized_end=741
  _SEARCHUSERREQUEST._serialized_start=743
  _SEARCHUSERREQUEST._serialized_end=779
  _SEARCHUSERRESPONSE._serialized_start=781
  _SEARCHUSERRESPONSE._serialized_end=843
  _FINDUSERBYEMAILREQUEST._serialized_start=845
  _FINDUSERBYEMAILREQUEST._serialized_end=889
  _FINDUSERBYEMAILRESPONSE._serialized_start=891
  _FINDUSERBYEMAILRESPONSE._serialized_end=958
  _GETUSERSRESPONSE._serialized_start=960
  _GETUSERSRESPONSE._serialized_end=1020
  _SETUSERSTATUSREQUEST._serialized_start=1022
  _SETUSERSTATUSREQUEST._serialized_end=1060
  _PINGREQUEST._serialized_start=1062
  _PINGREQUEST._serialized_end=1075
  _GETCLIENTSSTATUSREQUEST._serialized_start=1077
  _GETCLIENTSSTATUSREQUEST._serialized_end=1175
  _MEMBERINFOREQUEST._serialized_start=1177
  _MEMBERINFOREQUEST._serialized_end=1241
  _GETCLIENTSSTATUSRESPONSE._serialized_start=1243
  _GETCLIENTSSTATUSRESPONSE._serialized_end=1310
  _MEMBERINFORES._serialized_start=1313
  _MEMBERINFORES._serialized_end=1449
  _UPLOADAVATARREQUEST._serialized_start=1451
  _UPLOADAVATARREQUEST._serialized_end=1556
  _UPLOADAVATARRESPONSE._serialized_start=1558
  _UPLOADAVATARRESPONSE._serialized_end=1598
  _MFABASERESPONSE._serialized_start=1600
  _MFABASERESPONSE._serialized_end=1668
  _MFASTATERESPONSE._serialized_start=1670
  _MFASTATERESPONSE._serialized_end=1723
  _MFAGETSTATEREQUEST._serialized_start=1725
  _MFAGETSTATEREQUEST._serialized_end=1745
  _MFACHANGINGSTATEREQUEST._serialized_start=1747
  _MFACHANGINGSTATEREQUEST._serialized_end=1772
  _MFAAUTHCHALLENGEREQUEST._serialized_start=1774
  _MFAAUTHCHALLENGEREQUEST._serialized_end=1822
  _MFAAUTHCHALLENGERESPONSE._serialized_start=1824
  _MFAAUTHCHALLENGERESPONSE._serialized_end=1892
  _MFAVALIDATEPASSWORDREQUEST._serialized_start=1894
  _MFAVALIDATEPASSWORDREQUEST._serialized_end=1979
  _MFAVALIDATEOTPREQUEST._serialized_start=1981
  _MFAVALIDATEOTPREQUEST._serialized_end=2017
  _MFARESENDOTPREQUEST._serialized_start=2019
  _MFARESENDOTPREQUEST._serialized_end=2040
  _WORKSPACEUPDATEDISPLAYNAMEREQUEST._serialized_start=2042
  _WORKSPACEUPDATEDISPLAYNAMEREQUEST._serialized_end=2116
  _USER._serialized_start=2119
  _USER._serialized_end=3739
# @@protoc_insertion_point(module_scope)
