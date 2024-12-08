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

class MatchDetailSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    team1 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    team2 = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    scheduled_time = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = [
            'id', 'event', 'team1', 'team2', 'scheduled_time',
            'result', 'status'
            ]

    def update(self, instance, validated_data):
        """
        Handle updates for Match, ensuring related fields are assigned as instances.
        """
        # Update simple fields
        instance.scheduled_time = validated_data.get('scheduled_time', instance.scheduled_time)
        instance.result = validated_data.get('result', instance.result)
        instance.status = validated_data.get('status', instance.status)

        # Assign related instances
        instance.event = validated_data.get('event', instance.event)
        instance.team1 = validated_data.get('team1', instance.team1)
        instance.team2 = validated_data.get('team2', instance.team2)

        # Save the instance
        instance.save()
        return instance

    def get_scheduled_time(self, obj):
        return obj.scheduled_time.strftime('%Y-%m-%d %H:%M:%S')
