from rest_framework import generics, permissions
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer


# Team views
class TeamsView(generics.ListCreateAPIView):
    """
    List all teams or create a new team.
    """
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TeamDetailView(generics.RetrieveAPIView):
    """
    Show details of a specific team by ID.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# Player views
class PlayersView(generics.ListCreateAPIView):
    """
    List all players or create a new player.
    """
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PlayerDetailView(generics.RetrieveAPIView):
    """
    Show details of a specific player by ID.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
