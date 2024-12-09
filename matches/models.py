from django.db import models
from teams.models import Team
from events.models import Event


class Match(models.Model):
    STATUS_CHOISES = [
        ('upcoming', 'Upcoming'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name="matches")
    team1 = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name="team1_matches")
    team2 = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name="team2_matches")
    scheduled_time = models.DateTimeField()
    result = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default='upcoming')

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} ({self.status})"
