from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Player model.
    """
    avatar = serializers.URLField(
        required=False, allow_null=True, allow_blank=True
    )
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['id', 'name', 'role', 'avatar', 'team', 'team_name']

    def get_team_name(self, obj):
        """
        Returns the name of the team the player belongs to.
        If the player has no team, returns 'Unassigned'.
        """
        return obj.team.name if obj.team else "Unassigned"

    def validate_avatar(self, value):
        """
        Validates the 'avatar' field to ensure it's a valid URL or null.
        """
        if isinstance(value, str) and value.startswith("http"):
            return value
        if value is None:
            return value
        raise serializers.ValidationError(
            "Invalid avatar format. Provide a valid URL."
        )


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the Team model.
    """
    logo = serializers.URLField(
        required=False, allow_null=True, allow_blank=True
    )
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'logo', 'players']

    def validate_logo(self, value):
        """
        Validates the 'logo' field to ensure it's a valid URL or null.
        """
        if isinstance(value, str) and value.startswith("http"):
            return value  # Accept valid URLs
        if value is None:
            return value  # Allow null values
        raise serializers.ValidationError(
            "Invalid logo format. Provide a valid URL."
        )
