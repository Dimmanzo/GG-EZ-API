from django.db import models
from cloudinary.models import CloudinaryField
from urllib.parse import urlparse

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
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="players")

    def save(self, *args, **kwargs):
        if self.avatar:
            avatar_str = str(self.avatar)

            # If the avatar contains a full Cloudinary URL
            if "res.cloudinary.com" in avatar_str:
                parsed_url = urlparse(avatar_str)
                # Extract the relative path after '/image/upload/'
                if "image/upload/" in parsed_url.path:
                    relative_path = parsed_url.path.split("image/upload/")[-1]
                    self.avatar = f"image/upload/{relative_path}"
                else:
                    # Store the path as-is if it's already relative
                    self.avatar = parsed_url.path.lstrip("/")

        # Assign the default avatar if none is provided
        if not self.avatar or str(self.avatar).strip() == "":
            self.avatar = DEFAULT_PLAYER_AVATAR

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
