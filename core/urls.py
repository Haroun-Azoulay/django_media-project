from django.urls import path

from . import views

urlpatterns = [
    path("ping", views.health_check, name="health"),
    path("version", views.version_view, name="version"),
]
