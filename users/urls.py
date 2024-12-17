from django.urls import path
from .views import CurrentUserRoleView, CustomRegisterView


urlpatterns = [
    path(
        'dj-rest-auth/registration/',
        CustomRegisterView.as_view(),
        name='custom_registration'
    ),
    path(
        "current-user-role/",
        CurrentUserRoleView.as_view(),
        name="current-user-role"
    ),
]
