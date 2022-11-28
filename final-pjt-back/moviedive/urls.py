"""moviedive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/accounts/', include('accounts.urls')),
    path('api/accounts/', include('dj_rest_auth.urls')), 
    path('api/accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('api/accounts/password_change/', include('dj_rest_auth.registration.urls')),
    path('api/accounts/password_change/done/', include('dj_rest_auth.registration.urls')),
    path('api/accounts/password_reset/', include('dj_rest_auth.registration.urls')),
    path('api/accounts/password_reset/done/', include('dj_rest_auth.registration.urls')),
    path('api/movies/', include('movies.urls')),
    path('api/collections/', include('collects.urls')),
    path('api/community/', include('community.urls')),
    path('api/games/', include('games.urls')),
]
