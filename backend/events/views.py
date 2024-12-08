from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from rest_framework.exceptions import NotFound
from .models import Event
from .serializers import EventSerializer


class EventListView(generics.ListCreateAPIView):
    """
    List all events ordered by start date or create new events if logged in as admin.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('start_date')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filter fields
    filterset_fields = ['start_date', 'end_date']
    search_fields = ['name', 'description']
    ordering_fields = ['start_date', 'end_date']

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Only admins can create events.")
        serializer.save()
