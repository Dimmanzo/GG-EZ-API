from django.urls import path
from .views import TeamsView, PlayersView


urlpatterns = [
    path('', TeamsView.as_view(), name='team-list'),
    path('players/', PlayersView.as_view(), name='player-list'),
]