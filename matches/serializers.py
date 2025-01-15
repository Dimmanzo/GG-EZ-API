from django.utils.timezone import now
from rest_framework import serializers
from .models import Match
from teams.models import Team
from events.models import Event
from teams.serializers import TeamSerializer
from events.serializers import EventSerializer


class MatchSerializer(serializers.ModelSerializer):
    """
    Serializer for listing matches with additional event and team information.
    Includes event names and team names for better readability on the frontend.
    """
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    team1 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    team2 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    # Additional fields for easier access to related names
    scheduled_time = serializers.SerializerMethodField()
    event_name = serializers.SerializerMethodField()
    team1_name = serializers.SerializerMethodField()
    team2_name = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = [
            'id', 'event', 'event_name', 'team1', 'team1_name',
            'team2', 'team2_name', 'scheduled_time', 'result', 'status'
        ]

    def get_event_name(self, obj):
        return obj.event.name if obj.event else None

    def get_team1_name(self, obj):
        return obj.team1.name if obj.team1 else None

    def get_team2_name(self, obj):
        return obj.team2.name if obj.team2 else None

    def get_scheduled_time(self, obj):
        return obj.scheduled_time.strftime('%Y-%m-%d %H:%M:%S')


class MatchCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new match.
    """
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    team1 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    team2 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Match
        fields = ['id', 'event', 'team1', 'team2', 'scheduled_time', 'status']

    def validate(self, data):
        """
        Custom validation for Match creation.
        """
        if data['team1'] == data['team2']:
            raise serializers.ValidationError(
                "Team1 and Team2 must be different."
            )
        if data['scheduled_time'] < now():
            raise serializers.ValidationError(
                "Scheduled time cannot be in the past."
            )
        return data


class MatchDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailed match view with team and event names.
    """
    event_name = serializers.SerializerMethodField()
    team1_name = serializers.SerializerMethodField()
    team2_name = serializers.SerializerMethodField()
    scheduled_time = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = [
            'id', 'event', 'event_name', 'team1', 'team1_name',
            'team2', 'team2_name', 'scheduled_time', 'result', 'status'
        ]

    def get_event_name(self, obj):
        return obj.event.name if obj.event else None

    def get_team1_name(self, obj):
        return obj.team1.name if obj.team1 else None

    def get_team2_name(self, obj):
        return obj.team2.name if obj.team2 else None

    def get_scheduled_time(self, obj):
        return obj.scheduled_time.strftime('%Y-%m-%d %H:%M:%S')
