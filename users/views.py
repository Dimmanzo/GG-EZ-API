from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

# Retrieve the custom user model
User = get_user_model()


class CustomRegisterView(RegisterView):
    """
    Custom registration view that uses the CustomRegisterSerializer.
    Allows additional fields like 'role' during user registration.
    """
    serializer_class = CustomRegisterSerializer


class CurrentUserRoleView(APIView):
    """
    View to retrieve the currently authenticated user's details.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Handle GET requests to return user details.
        """
        user = request.user
        return Response({
            "username": user.username,
            "role": user.role,
            "email": user.email,
        })
