from django.urls import path
from .views import CustomRegisterView

urlpatterns = [
    path('dj-rest-auth/registration/', CustomRegisterView.as_view(), name='custom_registration'),
]
