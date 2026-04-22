"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import os
from django.contrib import admin
from django.urls import path, re_path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter


# DRF router for API root
router = DefaultRouter()

# Helper to get Codespace URL prefix
def get_api_url_prefix():
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        return f"https://{codespace_name}-8000.app.github.dev/api/"
    return "/api/"

def api_response(request, component):
    prefix = get_api_url_prefix()
    return JsonResponse({"url": f"{prefix}{component}/"})

urlpatterns = [
    path('', include(router.urls)),  # DRF API root at /
    path('admin/', admin.site.urls),
    re_path(r'^api/(?P<component>users|teams|activities|leaderboard|workouts)/$', api_response),
]
