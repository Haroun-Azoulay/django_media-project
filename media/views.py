from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .serializers import *
import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()


class UploadMedia(APIView):
    @extend_schema(
        summary="upload video",
        description="",
        # responses={"200": },
        tags=["media"],
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "file": {"type": "string", "format": "binary"},
                    "file_name": {"type": "string"},
                },
                "required": ["file", "file_name"],
            }
        },
    )
    def post(self, request):
        file = request.FILES.get("file")
        fileName = request.data.get("fileName")
        url = os.getenv("URL_UPLOAD")
        private_key = os.getenv("PRIVATE_KEY")
        auth_header = base64.b64encode(f"{private_key}:".encode()).decode()

        files = {"file": (file)}

        data = {"fileName": fileName}

        headers = {
            "Authorization": f"Basic {auth_header}",
            "Accept": "application/json",
        }

        response = requests.post(url, files=files, data=data, headers=headers)
        return Response(response.json(), status=response.status_code)
