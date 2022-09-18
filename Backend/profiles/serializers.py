from rest_framework import serializers

from core import settings
from .models import CustomProfile, Address
from versatileimagefield.serializers import VersatileImageFieldSerializer


class RetrieveProfileSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='BASIC_IMAGE_SET')

    class Meta:
        model = CustomProfile
        fields = ('first_name',
                  'last_name',
                  'birth_date',
                  'gender',
                  'image')


class UpdateProfileSerializer(RetrieveProfileSerializer):
    birth_date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('custom_profile',
                  'street_name',
                  'city_name',
                  'apartment_num',
                  'house_num',
                  'address_type',
                  'default_use',
                  'country',
                  'zip')


class RetrieveAddressSerializer(AddressSerializer):
    class Meta(AddressSerializer.Meta):
        fields = AddressSerializer.Meta.fields + ('id',)
