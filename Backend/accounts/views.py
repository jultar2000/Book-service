from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import account_activation_token
from .services import create_user
from .serializers import RegisterUserSerializer
from utils.exceptionhandler import CustomApiException

from django.utils.encoding import force_str

custom_user = get_user_model()


class SignUpView(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        create_user(request)
        return Response({'Successful registration': 'Please confirm your email to complete registration.'},
                        status=status.HTTP_201_CREATED)


class ActivateAccount(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = custom_user.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, custom_user.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response('Account confirmation successful', status=status.HTTP_200_OK)
        else:
            raise CustomApiException(400, 'Invalid token, token may been already used.')
