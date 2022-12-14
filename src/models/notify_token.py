import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import desc
from utils.logger import *
from src.models.base import Database

import logging
logger = logging.getLogger(__name__)
class NotifyToken(Database.get().Model):
    __tablename__ = 'notify_token'
    id = Database.get().Column(Database.get().String(36), primary_key=True)
    client_id = Database.get().Column(Database.get().String(36), ForeignKey('user.id'))
    device_id = Database.get().Column(Database.get().String(255), nullable=False)
    device_type = Database.get().Column(Database.get().String(16), nullable=False)
    push_token = Database.get().Column(Database.get().String(255), nullable=True)
    created_at = Database.get().Column(Database.get().DateTime, default=datetime.now)
    updated_at = Database.get().Column(Database.get().DateTime, onupdate=datetime.now)
    user = relationship('User', back_populates='tokens')
    end_user_env = Database.get().Column(Database.get().String(16))

    def add(self):
        client_device = self.get(self.client_id, self.device_id)
        if client_device is not None:
            self.id = client_device.id
            self.update()
        else:
            self.id = str(uuid.uuid4())
            try:
                Database.get_session().add(self)
                Database.get_session().commit()
            except Exception as e:
                Database.get_session().rollback()
                logger.error(e, exc_info=True)
        return self

    def get(self, client_id, device_id):
        client_device = Database.get_session().query(NotifyToken) \
            .filter(NotifyToken.client_id == client_id, NotifyToken.device_id == device_id) \
            .one_or_none()
        Database.get().session.remove()
        return client_device

    def get_client(self, client_id):
        client_tokens = Database.get_session().query(NotifyToken) \
            .filter(NotifyToken.client_id == client_id) \
            .order_by(desc(NotifyToken.created_at)) \
            .limit(1) \
            .all()
        Database.get().session.remove()
        return client_tokens

    def get_client_device_ids(self, client_id):
        client_tokens = Database.get_session().query(NotifyToken) \
            .filter(NotifyToken.client_id == client_id) \
            .order_by(desc(NotifyToken.created_at)) \
            .all()
        Database.get().session.remove()
        return client_tokens

    def get_clients(self, client_ids):
        client_tokens = Database.get_session().query(NotifyToken) \
            .filter(NotifyToken.client_id.in_(client_ids)) \
            .all()
        Database.get().session.remove()
        return client_tokens

    def update(self):
        try:
            Database.get_session().merge(self)
            Database.get_session().commit()
        except Exception as e:
            Database.get_session().rollback()
            logger.error(e, exc_info=True)

    def delete(self):
        try:
            Database.get_session().delete(self)
            Database.get_session().commit()
        except Exception as e:
            Database.get_session().rollback()
            logger.error(e, exc_info=True)
