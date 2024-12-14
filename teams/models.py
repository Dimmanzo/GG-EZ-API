from django.db import models
from cloudinary.models import CloudinaryField

DEFAULT_TEAM_LOGO = "image/upload/v1734180783/gg-ez/defaults/xgtwsoqklrrtgyeqcgq0.webp"
DEFAULT_PLAYER_AVATAR = "image/upload/v1734180756/gg-ez/defaults/vlhxug3hav82zlm6thbf.webp"

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = CloudinaryField('image', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.logo or str(self.logo).startswith("https://res.cloudinary.com/dzidcvhig/"):
            self.logo = DEFAULT_TEAM_LOGO
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    avatar = CloudinaryField('image', blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")

    def save(self, *args, **kwargs):
        if not self.avatar or str(self.avatar).startswith("https://res.cloudinary.com/dzidcvhig/"):
            self.avatar = DEFAULT_PLAYER_AVATAR
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
