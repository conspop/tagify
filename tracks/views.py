
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from .models import Track
from .serializers import TrackSerializer

class TracksList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tracks = Track.objects.filter(user=request.user)
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
