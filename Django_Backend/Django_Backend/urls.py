"""
URL configuration for Django_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


schema_view = get_schema_view(
    title="API Schema", description="Guide for the REST API")

swagger_view = TemplateView.as_view(
    template_name="Swagger.html", extra_context={"schema_url": "api_schema"}
)

app_patterns = [
    path('marketing-system/', include('Marketing_System.urls')),
]


urlpatterns = [
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.urls')),
    path('api_schema/', schema_view, name='api_schema'),
    path('', swagger_view, name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include(app_patterns)),
]
