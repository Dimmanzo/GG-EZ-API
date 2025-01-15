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
    )

    description = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "blank": "Event description cannot be blank.",
            "required": "Event description is required."
        }
    )

    class Meta:
        model = Event
        fields = [
            'id', 'name', 'description', 'start_date', 'end_date', 'image'
        ]

    # Validation for 'name'
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Event name cannot be blank.")
        if len(value) < 3:
            raise serializers.ValidationError(
                "Event name must be at least 3 characters long."
            )
        return value

    # Validation for start_date and end_date
    def validate(self, data):
        if 'start_date' in data and 'end_date' in data:
            if data['start_date'] > data['end_date']:
                raise serializers.ValidationError(
                    {"end_date": "End date must be after the start date."}
                )
        return data

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
