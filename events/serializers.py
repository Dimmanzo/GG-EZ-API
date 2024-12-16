from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    image = serializers.URLField(
        required=False, 
        allow_null=True, 
        allow_blank=True
    )

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'image']

    def validate_image(self, value):
        """
        Validate that the image is either a URL or a valid file.
        """
        if isinstance(value, str) and value.startswith("http"):
            return value  # Accept URLs
        if value is None:
            return value  # Allow null values
        raise serializers.ValidationError("Invalid image format. Provide a valid URL.")
