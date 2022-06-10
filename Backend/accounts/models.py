from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, blank=False,
                                help_text="Username is needed, 40 characters or fewer.")
    password = models.CharField(max_length=128, blank=False)
    email = models.EmailField(unique=True, blank=False)
    is_active = models.BooleanField(default=False, blank=False)


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active))


account_activation_token = TokenGenerator()
