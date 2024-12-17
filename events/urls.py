from django.urls import path
from .views import EventsView, EventDetailView


urlpatterns = [
    path('', EventsView.as_view(), name='event-list'),
    path('<int:pk>', EventDetailView.as_view(), name='event-detail'),
]
