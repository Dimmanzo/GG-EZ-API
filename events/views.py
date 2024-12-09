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

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Only admins can create events.")
        serializer.save()

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

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if not request.user.is_staff:
            return Response(
                {"detail": "Only admins can delete event."},
                status=status.HTTP_403_FORBIDDEN
            )
        obj.delete()
        return Response({"detail": f"Event '{obj.name}' deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            return Response(
                {"detail": "Only admins can update events."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save()
