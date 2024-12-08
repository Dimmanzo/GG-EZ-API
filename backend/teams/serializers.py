from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'role', 'avatar', 'team', 'team_name']

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'logo', 'players']