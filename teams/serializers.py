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

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Player name cannot be blank.")
        return value

    def validate_role(self, value):
        if not value.strip():
            raise serializers.ValidationError("Player role cannot be blank.")
        return value

    def validate_avatar(self, value):
        if not value or value in [None, ""]:
            return value
        if isinstance(value, str) and value.startswith("http"):
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

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Team name cannot be blank.")
        return value

    def validate_description(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Team description cannot be blank.")
        if len(value) < 10:
            raise serializers.ValidationError(
                "Team description must be at least 10 characters long."
            )
        return value

    def validate_logo(self, value):
        """
        Validates the 'logo' field to ensure it's a valid URL, null, or blank.
        """
        if not value or value in [None, ""]:
            return value  # Allow blank or null values; the model's save() will handle defaults.
        if isinstance(value, str) and value.startswith("http"):
            return value  # Accept valid URLs starting with 'http'.
        raise serializers.ValidationError(
            "Invalid logo format. Provide a valid URL."
        )
