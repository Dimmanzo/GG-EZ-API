"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from teams.views import PlayersView, PlayerDetailView
from .views import root_route, logout_route, upload_to_cloudinary

urlpatterns = [
    # Root route (landing page or default view)
    path('', root_route),
    # Admin interface
    path('admin/', admin.site.urls),
    # Authentication routes
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # Application routes
    path('', include('users.urls')),
    path('matches/', include('matches.urls')),
    path('events/', include('events.urls')),
    path('teams/', include('teams.urls')),
    # Player-specific views
    path('players/', PlayersView.as_view(), name='player-list'),
    path(
        'players/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'
    ),
    # Cloudinary upload proxy
    path("cloudinary-proxy/", upload_to_cloudinary, name="cloudinary_proxy"),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
