from src.models.signal_peer_key import PeerClientKey
from src.models.signal_group_key import GroupClientKey
from src.services.base import BaseService
from src.services.message import client_message_queue
from src.services.notify_inapp import NotifyInAppService
from src.models.group import GroupChat
from msg.message import Message
from utils.logger import *
import json
from msg.message import Message

import logging
logger = logging.getLogger(__name__)
client_queue = {}


class SignalService(BaseService):
    """
    SignalService, handling register/update/get/delete client peer/group key
    """
    def __init__(self):
        super().__init__(None)
        self.group_client_key_model = GroupClientKey()
        self.peer_model = PeerClientKey()
        self.group_chat_model = GroupChat()

    def peer_register_client_key(self, client_id, request):
        # register peer key for new client_id, with fully information of a peer key
        try:
            client_peer_key = PeerClientKey().set_key(client_id, request.registrationId, request.deviceId,
                                                      request.identityKeyPublic, request.preKeyId, request.preKey,
                                                      request.signedPreKeyId, request.signedPreKey,
                                                      request.signedPreKeySignature, request.identityKeyEncrypted)
            key_added = client_peer_key.add()
            # Check chatting available and push notify inapp for refreshing key, this should be unneeded as client_id now must register peer key when create account
            self.client_update_key_notify(client_id)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise Exception(Message.REGISTER_CLIENT_SIGNAL_KEY_FAILED)

    def client_update_peer_key(self, client_id, request):
        # update peer key for client_id, with fully information of a new peer key
        client = self.peer_model.get_by_client_id(client_id)
        if client is None:
            raise Exception(Message.UPDATE_CLIENT_SIGNAL_KEY_FAILED)

        client.set_key(client_id, request.registrationId, request.deviceId,
                          request.identityKeyPublic, request.preKeyId, request.preKey,
                          request.signedPreKeyId, request.signedPreKey,
                          request.signedPreKeySignature, request.identityKeyEncrypted
                          )
        client.update()
        # Check chatting available and push notify inapp for refreshing key
        self.client_update_key_notify(client_id)

    def client_update_identity_key(self, client_id, identity_key_encrypted):
        # update identity_key_encrypted of peer key for client_id, useful when changing password - which should make identity_key_encrypted changing too
        # return old identity_key_encrypted for get back in case needed
        client = self.peer_model.get_by_client_id(client_id)
        if client is None:
            raise Exception(Message.UPDATE_CLIENT_SIGNAL_KEY_FAILED)

        old_identity_key_encrypted = client.identity_key_encrypted
        client.identity_key_encrypted = identity_key_encrypted
        client.update()
        return old_identity_key_encrypted

    def peer_get_client_key(self, client_id):
        # get peer key of client_id
        return self.peer_model.get_by_client_id(client_id)

    def group_register_client_key(self, client_id, request):
        # register a group key for client_id
        client_group_key = GroupClientKey().set_key(
            request.groupId,
            client_id,
            None,
            None,
            request.deviceId,
            request.clientKeyDistribution,
            request.senderKeyId,
            request.senderKey,
            request.publicKey,
            request.privateKey
        )
        new_group_key = client_group_key.add()
        if new_group_key is None:
            raise Exception(Message.REGISTER_CLIENT_GROUP_FAILED_AVAILABLE)

    def group_bulk_update_client_key(self, client_id, group_client_keys):
        # update client_id's multi group keys
        group_ids = [
            key.groupId
            for key in group_client_keys
        ]
        keys = self.group_client_key_model.list_by_user_id_group_ids(client_id, group_ids)

        field_mapping = {
            'groupId': 'group_id',
            'deviceId': 'device_id',
            'clientKeyDistribution': 'client_key',
            'senderKeyId': 'client_sender_key_id',
            'senderKey': 'client_sender_key',
            'publicKey': 'client_public_key',
            'privateKey': 'client_private_key'

        }
        for key in keys:
            for _key in group_client_keys:
                if key.group_id != _key.groupId:
                    continue
                for name in field_mapping.keys():
                    if getattr(_key, name):
                        setattr(key, field_mapping[name], getattr(_key, name))
        self.group_client_key_model.bulk_update(keys)

    def group_get_client_key(self, group_id, client_id):
        # get client_id's group key in group_id
        client_key = self.group_client_key_model.get(group_id, client_id)
        if client_key:
            return client_key
        return None

    def group_by_owner_get_client_key(self, group_id, client_id):
        # get client_id's group key in owner_group with group_id
        client_key = self.group_chat_model.get_client_key_by_owner_group(group_id, client_id)
        if client_key:
            return client_key
        return None

    def group_get_all_client_key(self, group_id):
        # get all client's group keys in group_id
        return self.group_client_key_model.get_all_in_group(group_id)

    def client_update_key_notify(self, client_id):
        # list all client in peer chat with client_id about client_id's updating key event
        try:
            lst_group_peer = self.group_chat_model.get_joined_group_type(client_id, "peer")
            notify_inapp_service = NotifyInAppService()
            for group_peer in lst_group_peer:
                if group_peer.group_clients:
                    lst_client_id = json.loads(group_peer.group_clients)
                    for client_peer_id in lst_client_id:
                        if client_peer_id['id'] != client_id:
                            notify_inapp_service.notify_client_update_peer_key(client_peer_id['id'], client_id, group_peer.id)
        except Exception as e:
            logger.error(e, exc_info=True)

    def delete_client_peer_key(self, client_id):
        # delete a client peer key
        client_peer_key = self.peer_model.get_by_client_id(client_id)
        client_peer_key.delete()
        return True
