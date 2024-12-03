from rest_framework import serializers
from .models import Match
from teams.models import Team
from events.models import Event


class MatchSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.name')
    team1_name = serializers.CharField(source='team1.name')
    team2_name = serializers.CharField(source='team2.name')
    scheduled_time = serializers.SerializerMethodField() 

    class Meta:
        model = Match
        fields = [
            'id', 'event_name', 'team1_name', 'team2_name',
            'scheduled_time', 'status'
        ]

    def get_scheduled_time(self, obj):
        return obj.scheduled_time.strftime('%Y-%m-%d %H:%M:%S')

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
