from src.controllers.base import ErrorResponse
class Message:
    UNAUTHENTICATED = 1000
    AUTH_USER_NOT_FOUND = 1001
    REGISTER_USER_ALREADY_EXISTS = 1002
    REGISTER_USER_FAILED = 1003
    CHANGE_PASSWORD_FAILED = 1004
    USER_NOT_FOUND = 1005
    UPDATE_USER_INFO_FAILED = 1006

    msg_dict = {
        UNAUTHENTICATED: "Authentication required",
        AUTH_USER_NOT_FOUND: "Login information is not correct. Please try again",
        REGISTER_USER_ALREADY_EXISTS: "Username or email is available",
        REGISTER_USER_FAILED: "Register account failed. Please try again",
        CHANGE_PASSWORD_FAILED: "Change password failed. please try again",
        USER_NOT_FOUND: "User information is not correct. Please try again",
        UPDATE_USER_INFO_FAILED: "Change user profile failed. please try again",
    }

    @staticmethod
    def get_message(code):
        return Message.msg_dict[code]

    @staticmethod
    def get_error_object(code):
        return ErrorResponse(code, Message.msg_dict[code])


