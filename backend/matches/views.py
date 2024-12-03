from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Match
from .serializers import MatchSerializer, MatchDetailSerializer


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

class MatchDetail(generics.RetrieveAPIView):
    """
    Retrieve details of a specific match by ID.
    """
    serializer_class = MatchDetailSerializer
    queryset = Match.objects.all()

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Match.DoesNotExist:
            raise NotFound(detail="No match found with the given ID.", code=404)

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)