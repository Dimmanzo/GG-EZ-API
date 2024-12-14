from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name
