from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class RefreshSongs(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.profile.access_token:
            songs = request.user.profile.refresh_tracks()
            return Response(songs, status=status.HTTP_200_OK)

        else:
            return Response(
                "Spotify not authorized", status=status.HTTP_400_BAD_REQUEST
            )
