from django.db import models
from cloudinary.models import CloudinaryField

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name
