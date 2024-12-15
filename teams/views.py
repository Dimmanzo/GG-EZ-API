from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from api.permissions import IsStaffOrReadOnly
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer

class TeamsView(generics.ListCreateAPIView):
    """
    List all teams or create a new team.
    """
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer
    permission_classes = [IsStaffOrReadOnly]

    # Filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Searching
    search_fields = ['name', 'description', 'players__name']

    # Ordering
    ordering_fields = ['name', 'description']

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Show details of a specific team by ID.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsStaffOrReadOnly]

class PlayersView(generics.ListCreateAPIView):
    """
    List all players or create a new player.
    """
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer
    permission_classes = [IsStaffOrReadOnly]

    # Filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Searching
    search_fields = ['name', 'role', 'team__name']

    # Ordering
    ordering_fields = ['name', 'role']

class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Show details of a specific player by ID.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsStaffOrReadOnly]