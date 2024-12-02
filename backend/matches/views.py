from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Match
from .serializers import MatchSerializer


class MatchesView(APIView):
    def get(self, request):
        status_filter = request.query_params.get('status')

        if status_filter:
            matches = Match.objects.filter(status=status_filter).order_by('scheduled_time')
        else:
            matches = Match.objects.all().order_by('scheduled_time')

        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
