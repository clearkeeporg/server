from datetime import datetime, timedelta

from sqlalchemy.orm import relationship
from src.models.base import Database

import logging
logger = logging.getLogger(__name__)
class AuthenSetting(Database.get().Model):
    __tablename__ = 'authen_setting'
    #kid
    id = Database.get().Column(Database.get().String(36), primary_key=True)
    require_action = Database.get().Column(Database.get().String(36), unique=False, default=0)
    # otp setting
    mfa_enable = Database.get().Column(Database.get().Boolean, unique=False, default=False)
    otp = Database.get().Column(Database.get().String(100), unique=False, nullable=True)
    otp_frozen_time = Database.get().Column(Database.get().DateTime, unique=False, default=datetime.min)
    otp_tried_time = Database.get().Column(Database.get().INTEGER, unique=False, default=0)
    otp_request_counter = Database.get().Column(Database.get().INTEGER, unique=False, default=0)
    token_valid_time = Database.get().Column(Database.get().DateTime, unique=False, nullable=True)

    def add(self):
        try:
            Database.get_session().add(self)
            Database.get_session().commit()
            return self
        except:
            Database.get_session().rollback()
            raise

    def update(self):
        try:
            Database.get_session().merge(self)
            Database.get_session().commit()
        except Exception as e:
            Database.get_session().rollback()
            logger.error(e, exc_info=True)

    def get(self, client_id):
        mfa_setting = Database.get_session().query(AuthenSetting) \
            .filter(AuthenSetting.id == client_id) \
            .one_or_none()
        Database.get().session.remove()
        return mfa_setting

    def __repr__(self):
        return '<Item(id=%s, mfa_enable=%s)>' % (self.id, self.mfa_enable)
