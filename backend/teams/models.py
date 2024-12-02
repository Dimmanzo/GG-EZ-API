from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


if settings.DEBUG:
    from django.db.models import ImageField as MediaField
else:
    MediaField = CloudinaryField

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = MediaField('image', blank=True, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    avatar = MediaField('image', blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.name
