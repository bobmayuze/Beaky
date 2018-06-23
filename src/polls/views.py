from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    print(request.method)
    request_keys = request.GET.keys()
    for key in request_keys:
        print(key, request.GET[key])
    # num = int(request.GET["num"])
    # print(request.GET["num"])
    return HttpResponse("Hello, world. You're at the polls index.")
    # return HttpResponse(num ** 2)

def foo(request, page = 1):
    return HttpResponse("Hello World")
