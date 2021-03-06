from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .services import create_user, activate_accounts, blacklist_token
from .serializers import RegisterUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

custom_user = get_user_model()


class SignUpView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            create_user(request)
            return Response({'Successful registration': 'Please confirm your email to complete registration.'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateAccount(APIView):
    def get(self, request, uidb64, token):
        activate_accounts(uidb64, token)
        return Response('Account confirmation successful', status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LogoutView(APIView):
    def post(self, request):
        blacklist_token(request.data)
        return Response('Logout successful', status=status.HTTP_205_RESET_CONTENT)
