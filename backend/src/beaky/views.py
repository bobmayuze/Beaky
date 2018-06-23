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


def signUp(request):
    if request.method == 'GET':
        return HttpResponse("Bad request")
    req_body = json.loads(request.body.decode('utf-8'))
    try:
        username = req_body["username"]
        password = req_body["password"]
        email = req_body["email"]
        labels = req_body["labels"]
        services.signUp(username, password, email, labels)
        return HttpResponse("Account created successfully")
    except Exception as e:
        print(e)
        return HttpResponse("Bad request")
