from django.db import models
from cloudinary.models import CloudinaryField

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    avatar = CloudinaryField('image', blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.name
