from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView

from .models import CustomProfile
from .serializers import UpdateProfileSerializer, RetrieveUserSerializer
from .services import update_profile
from rest_framework.response import Response
from rest_framework import status


class ProfileViewSet(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():
            update_profile(serializer.validated_data, request.user)
            return Response({'Account successfully updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        custom_profile = CustomProfile.objects.get(custom_user=request.user)
        serializer = RetrieveUserSerializer(custom_profile, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)
