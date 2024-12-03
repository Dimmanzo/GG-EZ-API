from django.urls import path
from .views import MatchesView, MatchDetail


urlpatterns = [
    path('', MatchesView.as_view(), name='matches'),
    path('<int:pk>/', MatchDetail.as_view(), name='match-detail'),
]