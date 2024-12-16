from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from api.permissions import IsStaffOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventsView(generics.ListCreateAPIView):
    """
    List all events ordered by start date or create new events if logged in as admin.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('start_date')
    permission_classes = [IsStaffOrReadOnly]

    # Filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filter fields
    search_fields = ['name', 'description', 'start_date', 'end_date']
    ordering_fields = ['start_date', 'end_date']

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Show details of a specific event by ID.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsStaffOrReadOnly]

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Event.DoesNotExist:
            raise NotFound(detail="No event found with the given ID.", code=404)

