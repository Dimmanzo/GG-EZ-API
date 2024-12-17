from django.db import models
from cloudinary.models import CloudinaryField

# Default URLs for team logos and player avatars
DEFAULT_TEAM_LOGO = "https://res.cloudinary.com/dzidcvhig/image/upload/v1734180783/gg-ez/defaults/xgtwsoqklrrtgyeqcgq0.webp"
DEFAULT_PLAYER_AVATAR = "https://res.cloudinary.com/dzidcvhig/image/upload/v1734180756/gg-ez/defaults/vlhxug3hav82zlm6thbf.webp"


class Team(models.Model):
    """
    Team with a name, description, and logo.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = CloudinaryField('image', blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Override save method to set a default logo if none is provided.
        """
        if not self.logo:
            self.logo = DEFAULT_TEAM_LOGO
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Player(models.Model):
    """
    Player with a name, role, avatar, and an optional team association.
    """
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    avatar = CloudinaryField('image', blank=True, null=True)
    team = models.ForeignKey(
        'Team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players"
    )

    def save(self, *args, **kwargs):
        """
        Override save method to set a default avatar if none is provided.
        """
        if not self.avatar:
            self.avatar = DEFAULT_PLAYER_AVATAR
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
