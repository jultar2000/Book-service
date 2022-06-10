from rest_framework import serializers

from core import settings
from .models import CustomProfile
from versatileimagefield.serializers import VersatileImageFieldSerializer


class UpdateProfileSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='BASIC_IMAGE_SET')
    birth_date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = CustomProfile
        fields = ('first_name',
                  'last_name',
                  'birth_date',
                  'gender',
                  'image')
