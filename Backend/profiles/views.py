from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UpdateProfileSerializer
from .services import update_profile
from rest_framework.response import Response
from rest_framework import status


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():
            update_profile(serializer.validated_data, request.user)
            return Response({'Account successfully updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
