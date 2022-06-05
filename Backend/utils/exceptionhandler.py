from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code


class CustomApiException(APIException):
    status_code = None
    detail = None

    def __init__(self, message, status_code):
        CustomApiException.status_code = status_code
        CustomApiException.detail = message
