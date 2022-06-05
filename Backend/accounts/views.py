from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .services import create_user, login_user, activate_accounts
from .serializers import RegisterUserSerializer, LoginUserSerializer

custom_user = get_user_model()


class SignUpView(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        create_user(request)
        return Response({'Successful registration': 'Please confirm your email to complete registration.'},
                        status=status.HTTP_201_CREATED)


class ActivateAccount(APIView):
    def get(self, request, uidb64, token):
        activate_accounts(uidb64, token)
        return Response('Account confirmation successful', status=status.HTTP_200_OK)


class SignInView(APIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        login_user(request)
        return Response({'Logging successful!'}, status=status.HTTP_200_OK)
