import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my GG-EZ API!"
    })


@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response

@csrf_exempt
def upload_to_cloudinary(request):
    """
    Proxy the file upload to Cloudinary to avoid CORS issues.
    """
    if request.method == "POST":
        try:
            file = request.FILES['file']
            upload_preset = "ml_default"

            cloudinary_url = "https://api.cloudinary.com/v1_1/dzidcvhig/image/upload"

            response = requests.post(
                cloudinary_url,
                data={"upload_preset": upload_preset},
                files={"file": (file.name, file.read(), file.content_type)}
            )
            
            return JsonResponse(response.json(), safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)