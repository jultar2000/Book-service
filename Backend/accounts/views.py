from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .services import create_user
from .serializers import RegisterUserSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        create_user(request.data)
        return Response({'Successful registration': 'Please confirm your email to complete registration.'},
                        status=status.HTTP_201_CREATED)
