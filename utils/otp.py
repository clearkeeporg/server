import os
import random
import string
import time
import datetime
import json
from jose import jws
from hashlib import md5
from hmac import compare_digest as compare_hash
from twilio.rest import Client
from utils.config import get_otp_server
from utils.logger import *

account_sid = get_otp_server()["twilio_account_sid"]
auth_token =  get_otp_server()["twilio_auth_token"]
client = Client(account_sid, auth_token)
life_time = datetime.timedelta(seconds=get_otp_server()["otp_life_time"])
message_form = 'Your OTP code is {}'
# set up a phone number for sending
code_length = get_otp_server()["otp_code_length"]
from_phone = get_otp_server()["otp_server_phone_number"]
secret_key = get_otp_server()["otp_secret_key"]

class OTPServer(object):
    valid_trying_time = get_otp_server()["input_otp_per_validate"]
    valid_resend_time = get_otp_server()["request_otp_server_per_day"]

    @staticmethod
    def get_otp(phone_number):
        otp = OTPServer._create_otp()
        logger.info('{} sent to {}'.format(message_form.format(otp), phone_number))
        OTPServer._otp_message_sending(otp, phone_number)
        return otp

    @staticmethod
    def _create_otp():
        otp = ''.join(random.choices(string.digits, k=code_length))
        return otp

    @staticmethod
    def get_valid_time():
        return datetime.datetime.now() + life_time

    @staticmethod
    def sign_message(kid, require_action):
        message = {
            "iss": kid,
            "aud": require_action,
            "exp": int(time.time()) + 86400
        }
        signed_message = jws.sign(message, secret_key, algorithm='HS256')
        return signed_message

    def verify_message(signed_message):
        message = json.loads(jws.verify(signed_message, secret_key, algorithms=['HS256']).decode('utf-8'))
        return message

    @staticmethod
    def hash_uid(kid, valid_time, require_action=''):
        secret_string = "{}{}{}{}".format(kid, valid_time, secret_key, require_action)
        hash_string = md5(secret_string.encode("utf-8")).hexdigest()
        pre_access_token = '.'.join([kid, hash_string])
        return hash_string

    @staticmethod
    def cal_frozen_time():
        return datetime.datetime.now().replace(hour=0, minute=0,second=0, microsecond=0) + datetime.timedelta(days=1)

    @staticmethod
    def verify_hash_code(kid, valid_time, pre_access_token, require_action=''):
        kid, hash_string = pre_access_token.split('.', 1)
        verify_secret_string = "{}{}{}{}".format(kid, valid_time, secret_key, require_action)
        verify_hash_string = md5(verify_secret_string.encode("utf-8")).hexdigest()
        return compare_hash(verify_hash_string, hash_string)

    @staticmethod
    def _otp_message_sending(otp, phone_number):
        try:
            message = client.messages.create(
                                      body=message_form.format(otp),
                                      from_=from_phone,
                                      to=phone_number
                                  )
            return True
        except Exception as e:
            # log e
            return False
