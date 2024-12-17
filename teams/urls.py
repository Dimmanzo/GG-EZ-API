from django.urls import path
from .views import TeamsView, PlayersView, TeamDetailView


urlpatterns = [
    path('', TeamsView.as_view(), name='team-list'),
    path('<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
]
