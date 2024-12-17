from django.db import models
from cloudinary.models import CloudinaryField

# Default event image URL to use if no image is provided
DEFAULT_EVENT_IMAGE = "https://res.cloudinary.com/dzidcvhig/image/upload/v1734180701/gg-ez/defaults/nou2mptttvfkmdtijdhu.webp"


class Event(models.Model):
    """
    Event with details such as name, description, dates, and an optional image.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    image = CloudinaryField('image', blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method.
        If no image is provided, assigns a default event image.
        """
        if not self.image:
            self.image = DEFAULT_EVENT_IMAGE
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
