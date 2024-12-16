from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        required=False, 
        allow_null=True, 
        use_url=True
    )

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'image']

    def get_image(self, obj):
        if obj.image:
            return f"https://res.cloudinary.com/dzidcvhig/{obj.image}"
        return None
