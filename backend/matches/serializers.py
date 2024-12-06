from rest_framework import serializers
from .models import Match
from teams.models import Team
from events.models import Event
from teams.serializers import TeamSerializer
from events.serializers import EventSerializer


class MatchSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    scheduled_time = serializers.SerializerMethodField() 

    class Meta:
        model = Match
        fields = [
            'id', 'event', 'team1', 'team2',
            'scheduled_time', 'status'
        ]

    def get_scheduled_time(self, obj):
        return obj.scheduled_time.strftime('%Y-%m-%d %H:%M:%S')

class MatchCreateSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    team1 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    team2 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Match
        fields = ['id', 'event', 'team1', 'team2', 'scheduled_time', 'status']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'logo']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'start_date', 'end_date']

class MatchDetailSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    event = EventSerializer()

    scheduled_time = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = [
            'id', 'event', 'team1', 'team2', 'scheduled_time',
            'result', 'status'
            ]

    def get_scheduled_time(self, obj):
        return obj.scheduled_time.strftime('%Y-%m-%d %H:%M:%S')
