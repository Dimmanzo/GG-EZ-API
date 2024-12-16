from rest_framework import serializers
from .models import Match
from teams.models import Team
from events.models import Event
from teams.serializers import TeamSerializer
from events.serializers import EventSerializer


class MatchSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    team1 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    team2 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
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
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    team1 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    team2 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Match
        fields = ['id', 'event', 'team1', 'team2', 'scheduled_time', 'status']

class MatchDetailSerializer(serializers.ModelSerializer):
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
