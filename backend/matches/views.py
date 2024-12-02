from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Match
from .serializers import MatchSerializer


class MatchesView(generics.ListAPIView):
    """
    List all matches or filter them by status and other parameters.
    """
    serializer_class = MatchSerializer
    queryset = Match.objects.all().order_by('scheduled_time')

    # Filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering, searching and ordering
    filterset_fields = ['status']
    search_fields = ['team1__name', 'team2__name', 'event__name']
    ordering_fields = ['sheduled_time', 'status', 'event__name']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            raise NotFound(detail="No matches found with the given criteria", code=404)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
