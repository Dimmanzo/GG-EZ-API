from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from api.permissions import IsStaffOrReadOnly
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer


class TeamsView(generics.ListCreateAPIView):
    """
    View to list all teams or create a new team.
    """
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer
    permission_classes = [IsStaffOrReadOnly]

    # Filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ['name', 'description', 'players__name']
    ordering_fields = ['name', 'description']


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific team by its ID.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsStaffOrReadOnly]


class PlayersView(generics.ListCreateAPIView):
    """
    View to list all players or create a new player.
    """
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer
    permission_classes = [IsStaffOrReadOnly]

    # Filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ['name', 'role', 'team__name']
    ordering_fields = ['name', 'role']


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific player by its ID.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsStaffOrReadOnly]
