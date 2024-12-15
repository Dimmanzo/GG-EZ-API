from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['id', 'name', 'role', 'avatar', 'team', 'team_name']

    def get_team_name(self, obj):
        return obj.team.name if obj.team else "Unassigned"

    def to_representation(self, instance):
        """Ensure avatar URL is always in full format with Cloudinary prefix."""
        representation = super().to_representation(instance)
        avatar = representation.get("avatar")

        if avatar and not avatar.startswith("https://res.cloudinary.com/"):
            representation["avatar"] = f"https://res.cloudinary.com/dzidcvhig/{avatar}"
        return representation


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'logo', 'players']

    def to_representation(self, instance):
        """Ensure logo URL is always in full format with Cloudinary prefix."""
        representation = super().to_representation(instance)
        logo = representation.get("logo")

        if logo and not logo.startswith("https://res.cloudinary.com/"):
            representation["logo"] = f"https://res.cloudinary.com/dzidcvhig/{logo}"
        return representation
