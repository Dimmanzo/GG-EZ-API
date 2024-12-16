from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(
        required=False, 
        allow_null=True, 
        use_url=True
    )
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
            representation["avatar"] = f"{avatar}"
        return representation


class TeamSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(
        required=False, 
        allow_null=True, 
        use_url=True
    )
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'logo', 'players']

    def to_representation(self, instance):
        """Ensure logo URL is always in full format with Cloudinary prefix."""
        representation = super().to_representation(instance)
        logo = representation.get("logo")

        if logo and not logo.startswith("https://res.cloudinary.com/"):
            representation["logo"] = f"{logo}"
        return representation
