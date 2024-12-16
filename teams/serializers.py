from rest_framework import serializers
from .models import Team, Player

class PlayerSerializer(serializers.ModelSerializer):
    avatar = serializers.URLField(required=False, allow_null=True, allow_blank=True)
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['id', 'name', 'role', 'avatar', 'team', 'team_name']

    def get_team_name(self, obj):
        return obj.team.name if obj.team else "Unassigned"

    def validate_avatar(self, value):
        """
        Validate the avatar field to allow URLs or null values.
        """
        if isinstance(value, str) and value.startswith("http"):
            return value  # Accept URLs
        if value is None:
            return value  # Allow null values
        raise serializers.ValidationError("Invalid avatar format. Provide a valid URL.")


class TeamSerializer(serializers.ModelSerializer):
    logo = serializers.URLField(required=False, allow_null=True, allow_blank=True)
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'logo', 'players']

    def validate_logo(self, value):
        """
        Validate the logo field to allow URLs or null values.
        """
        if isinstance(value, str) and value.startswith("http"):
            return value  # Accept URLs
        if value is None:
            return value  # Allow null values
        raise serializers.ValidationError("Invalid logo format. Provide a valid URL.")
