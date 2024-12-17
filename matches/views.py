from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from api.permissions import IsStaffOrReadOnly
from .models import Match
from .serializers import MatchSerializer, MatchDetailSerializer, MatchCreateSerializer


class MatchesView(generics.ListCreateAPIView):
    """
    View to list all matches or create a new match.
    """
    queryset = Match.objects.all().order_by('scheduled_time')
    permission_classes = [IsStaffOrReadOnly]

    # Filtering, searching, and ordering settings
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['status']
    search_fields = ['team1__name', 'team2__name', 'event__name']
    ordering_fields = ['scheduled_time', 'status', 'event__name']

    def get_serializer_class(self):
        """
        Returns the appropriate serializer based on the request method.
        """
        if self.request.method == 'POST':
            return MatchCreateSerializer
        return MatchSerializer


class MatchDetail(generics.RetrieveAPIView):
    """
    View to retrieve, update, or delete a specific match by ID.
    """
    serializer_class = MatchDetailSerializer
    queryset = Match.objects.all()
    permission_classes = [IsStaffOrReadOnly]

    def get_object(self):
        """
        Custom method to retrieve a match by ID.
        Raises a 404 error if the match does not exist.
        """
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Match.DoesNotExist:
            raise NotFound(
                detail="No match found with the given ID.", code=404
            )

    def get(self, request, *args, **kwargs):
        """
        Handles GET request to retrieve a single match.
        """
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """
        Handles PUT request to update a match's details.
        """
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Handles DELETE request to remove a match.
        """
        obj = self.get_object()
        obj.delete()
        return Response(
            {"detail": "Match deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
