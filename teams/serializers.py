from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'role', 'avatar', 'team', 'team_name']

    def to_representation(self, instance):
        """Ensure avatar URL is always in full format with Cloudinary prefix."""
        representation = super().to_representation(instance)
        avatar = representation.get("avatar")

        if avatar and not avatar.startswith("https://res.cloudinary.com/"):
            representation["avatar"] = f"https://res.cloudinary.com/dzidcvhig/{avatar}"
        return representation


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
