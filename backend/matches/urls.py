from django.urls import path
from .views import MatchesView


urlpatterns = [
    path('', MatchesView.as_view(), name='matches'),
]