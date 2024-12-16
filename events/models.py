from django.db import models
from cloudinary.models import CloudinaryField

DEFAULT_EVENT_IMAGE = "https://res.cloudinary.com/dzidcvhig/image/upload/v1734180701/gg-ez/defaults/nou2mptttvfkmdtijdhu.webp"

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    image = CloudinaryField('image', blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Ensure the image field accepts both Cloudinary URLs and the default image.
        """
        if not self.image:  # If no image is provided, set the default
            self.image = DEFAULT_EVENT_IMAGE
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
