import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import services


# Create your views here.
def index(request):
    print(request.method)
    request_keys = request.GET.keys()
    for key in request_keys:
        print(key, request.GET[key])
    return HttpResponse("Hello, world. You're at the polls index.")


def foo(request, page=1):
    return HttpResponse("Hello World")
