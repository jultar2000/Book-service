from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet

from .models import CustomProfile, Address
from .serializers import UpdateProfileSerializer, RetrieveProfileSerializer, AddressSerializer
from .services import update_profile, unset_default_address
from rest_framework.response import Response
from rest_framework import status


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():
            update_profile(serializer, request.user)
            return Response({'Account successfully updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        custom_profile = CustomProfile.objects.get(custom_user=request.user)
        serializer = RetrieveProfileSerializer(custom_profile, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddressView(ListModelMixin,
                  CreateModelMixin,
                  UpdateModelMixin,
                  GenericViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        profile = CustomProfile.objects.get(custom_user=request.user)
        queryset = Address.objects.filter(custom_profile=profile, default_use=True)
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            unset_default_address(request.user, serializer.validated_data.get('address_type'))
            serializer.create(serializer.validated_data)
            return Response({'Address successfully created'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
