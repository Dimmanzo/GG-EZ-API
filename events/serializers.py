from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model.
    """
    image = serializers.URLField(
        required=False,
        allow_null=True,
        allow_blank=True
    )  # Custom field to accept optional image URLs

    class Meta:
        model = Event
        fields = [
            'id', 'name', 'description', 'start_date', 'end_date', 'image'
        ]

    def validate_image(self, value):
        """
        Custom validator for the 'image' field.
        Ensures that the image is either a valid URL or left empty.
        """
        if isinstance(value, str) and value.startswith("http"):
            return value  # Accept URLs starting with 'http'
        if value is None:
            return value  # Allow null values for the image field
        raise serializers.ValidationError(
            "Invalid image format. Provide a valid URL."
        )
        # Raises an error if the input is not a valid URL or empty
