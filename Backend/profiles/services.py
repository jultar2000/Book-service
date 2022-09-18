from utils.exceptionhandler import CustomApiException
from .models import CustomProfile, Address


def update_profile(serializer, user):
    try:
        custom_profile = CustomProfile.objects.get(custom_user=user)
    except CustomProfile.DoesNotExist:
        raise CustomApiException("Custom Profile does not exist", 400)
    serializer.update(custom_profile, serializer.validated_data)


def retrieve_address(user, pk):
    try:
        return Address.objects.get(custom_user=user, pk=pk)
    except Address.DoesNotExist:
        raise CustomApiException("Address does not exist", 400)


def unset_default_address(user, address_type):
    try:
        custom_profile = CustomProfile.objects.get(custom_user=user)
        address = Address.objects.get(custom_profile=custom_profile, address_type=address_type, default_use=True)
        address.default_use = False
        address.save()
    except Address.DoesNotExist:
        pass
