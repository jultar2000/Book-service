from rest_framework import serializers
from django.contrib.auth import get_user_model

custom_user = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)

    class Meta:
        model = custom_user
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = custom_user
        fields = ('username', 'password')
