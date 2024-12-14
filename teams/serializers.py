from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['id', 'name', 'role', 'avatar', 'team', 'team_name']

    def get_avatar(self, obj):
        if obj.avatar:
            return f"https://res.cloudinary.com/dzidcvhig/{obj.avatar}"
        return None


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'logo', 'players']

    def get_logo(self, obj):
        if obj.logo:
            return f"https://res.cloudinary.com/dzidcvhig/{obj.logo}"
        return None
