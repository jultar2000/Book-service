from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

custom_user = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)

    class Meta:
        model = custom_user
        fields = ('username', 'email', 'password1', 'password2')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
