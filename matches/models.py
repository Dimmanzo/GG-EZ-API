from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from teams.models import Team
from events.models import Event


class Match(models.Model):
    """
    Represents a match between two teams within a specific event.
    Includes details such as scheduled time, result, and match status.
    """

    # Choices for the match status
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    # Relationships
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name="matches"
    )
    team1 = models.ForeignKey(
        'teams.Team',
        on_delete=models.CASCADE,
        related_name="team1_matches"
    )
    team2 = models.ForeignKey(
        'teams.Team',
        on_delete=models.CASCADE,
        related_name="team2_matches"
    )

    # Match details
    scheduled_time = models.DateTimeField()
    result = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='upcoming'
    )

    class Meta:
        verbose_name_plural = "Matches"

    def clean(self):
        """
        Custom validation to ensure data integrity.
        """
        if self.team1 == self.team2:
            raise ValidationError("Team1 and Team2 cannot be the same.")
        if self.scheduled_time < now():
            raise ValidationError("Scheduled time cannot be in the past.")

    def save(self, *args, **kwargs):
        """
        Call clean() before saving to enforce custom validations.
        """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} ({self.status})"
