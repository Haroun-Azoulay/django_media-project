from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from . import __version__
from .serializers import *


class HealthCheckView(APIView):
    @extend_schema(
        summary="health check",
        description="Check the API is alive or not.",
        responses={"200": PingSerializer},
        tags=["core"],
    )
    def get(self, request):
        return Response({"message": "pong"})


class VersionView(APIView):
    @extend_schema(
        summary="Version",
        description="Get a version",
        responses={"200": VersionSerializer},
        tags=["core"],
    )
    def get(self, request):
        return Response({"version": __version__})
