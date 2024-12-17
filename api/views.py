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
    """
    Root endpoint to welcome users to the API.
    """
    return Response({
        "message": "Welcome to my GG-EZ API!"
    })


@api_view(['POST'])
def logout_route(request):
    """
    Handles user logout by clearing the JWT cookies.
    """
    response = Response()
    # Clear the JWT access cookie
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    # Clear the JWT refresh cookie
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
    Proxy endpoint for uploading files to Cloudinary.
    Avoids CORS issues by handling the upload on the server.
    Forwards the file from the client to the Cloudinary API.
    """
    if request.method == "POST":
        try:
            # Get the uploaded file from the request
            file = request.FILES['file']
            upload_preset = "ml_default"

            cloudinary_url = "https://api.cloudinary.com/v1_1/dzidcvhig/image/upload"

            # Send the file to Cloudinary via POST
            response = requests.post(
                cloudinary_url,
                data={"upload_preset": upload_preset},
                files={"file": (file.name, file.read(), file.content_type)}
            )

            # Return the Cloudinary response to the client
            return JsonResponse(response.json(), safe=False)

        except Exception as e:
            # Handle any errors during the upload process
            return JsonResponse({"error": str(e)}, status=500)

    # Return an error for unsupported request methods
    return JsonResponse({"error": "Invalid request method"}, status=400)
