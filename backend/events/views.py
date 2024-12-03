from rest_framework import generics
from .models import Event
from .serializers import EventSerializer


class EventListView(generics.ListAPIView):
    """
    List all events ordered by start date.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('start_date')
