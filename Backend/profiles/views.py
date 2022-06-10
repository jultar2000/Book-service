from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UpdateProfileSerializer
from .services import update_profile
from rest_framework.response import Response
from rest_framework import status


class UpdateProfileView(APIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):
        update_profile(request)
        return Response({'Account successfully updated'}, status=status.HTTP_200_OK)
