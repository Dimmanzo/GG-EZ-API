from django.db import models
from cloudinary.models import CloudinaryField

DEFAULT_EVENT_IMAGE = "image/upload/v1734180701/gg-ez/defaults/nou2mptttvfkmdtijdhu.webp"

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    image = CloudinaryField('image', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.image or str(self.image).startswith("https://res.cloudinary.com/dzidcvhig/"):
            self.image = DEFAULT_EVENT_IMAGE
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
