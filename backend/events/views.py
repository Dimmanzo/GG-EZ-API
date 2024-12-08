from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer


class EventListView(generics.ListCreateAPIView):
    """
    List all events ordered by start date, option to create new events for admins.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('start_date')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Only admins can create events.")
        serializer.save()
