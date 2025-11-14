from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import __version__

def health_check(request):
    return JsonResponse({"response":"pong"})

def version_view(request):
    return JsonResponse({"version": __version__})
