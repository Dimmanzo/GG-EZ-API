from rest_framework import generics
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer


# Team views
class TeamsView(generics.ListAPIView):
    """
    List all teams.
    """
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer

# Player views
class PlayersView(generics.ListAPIView):
    """
    List all players.
    """
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer
