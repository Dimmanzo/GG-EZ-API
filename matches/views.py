from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from api.permissions import IsStaffOrReadOnly
from .models import Match
from .serializers import MatchSerializer, MatchDetailSerializer, MatchCreateSerializer


class MatchesView(generics.ListCreateAPIView):
    """
    List all matches or create a new match if logged in as admin.
    """
    serializer_class = MatchSerializer
    queryset = Match.objects.all().order_by('scheduled_time')
    permission_classes = [IsStaffOrReadOnly]

    # Filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering, searching and ordering
    filterset_fields = ['status']
    search_fields = ['team1__name', 'team2__name', 'event__name']
    ordering_fields = ['sheduled_time', 'status', 'event__name']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MatchCreateSerializer
        return MatchDetailSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            return Response(
                {"detail": "Only admins can create matches."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save()

class MatchDetail(generics.RetrieveAPIView):
    """
    Retrieve, update, or delete a specific match by ID.
    """
    serializer_class = MatchDetailSerializer
    queryset = Match.objects.all()
    permission_classes = [IsStaffOrReadOnly]

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Match.DoesNotExist:
            raise NotFound(detail="No match found with the given ID.", code=404)

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response({"detail": "Match deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
