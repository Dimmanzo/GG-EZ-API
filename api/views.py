from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes, api_view
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to the GG-EZ API!",
    })


@csrf_exempt
@api_view(['POST'])
def logout_route(request):
    response = Response({"message": "Logged out"})
    response.delete_cookie("my-app-auth")
    response.delete_cookie("my-refresh-token")
    return response
