import json
from bson import ObjectId
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

def publish(request):
    if request.method == 'GET':
        return HttpResponse("Bad request")
    req_body = json.loads(request.body.decode('utf-8'))
    try:
        quesiton = req_body["quesiton"]
        size = req_body["size"]
        initial_pool = req_body["initial_pool"]
        audience_labels = sorted(req_body["audience_labels"])
        services.publishQuestion(quesiton,size, initial_pool, audience_labels)
        return HttpResponse("Question published successfully")
    except Exception as e:
        print(e)
        return HttpResponse("Bad request")


def vote(request):
    if request.method == 'GET':
        return HttpResponse("Bad request")
    req_body = json.loads(request.body.decode('utf-8'))
    try:
        choice = req_body["choice"]
        question_id = req_body["question_id"]
        result = services.voteQuestionById(question_id, choice)
        return HttpResponse(result)
    except Exception as e:
        print(e)
        return HttpResponse("Bad request")

def searchQuestionById(request):
    if request.method == 'GET':
        return HttpResponse("Bad request")
    req_body = json.loads(request.body.decode('utf-8'))
    try:
        question_id = req_body["question_id"]
        target_question = services.getQuestionById(question_id)
        return HttpResponse(
            json.dumps(target_question, ensure_ascii=False),
            content_type='application/json')
    except Exception as e:
        print(e)
        return HttpResponse("Bad request")


def searchQuestionByQuery(request):
    '''
    return: a list of questions associated with their object id to make sure we can retrive the whole object
    '''
    if request.method == 'GET':
        return HttpResponse("Bad request")
    req_body = json.loads(request.body.decode('utf-8'))
    try:
        questions = req_body["questions"]
        labels = req_body["labels"]
        return HttpResponse("TODD: This functions is not implemented yet")
    except Exception as e:
        print(e)
        return HttpResponse("Bad request")


def searchQuestionByLabels(request):
    '''
    return: a list of questions associated with the specific labes in the request
    '''
    if request.method == 'GET':
        return HttpResponse("Bad request")
    req_body = json.loads(request.body.decode('utf-8'))
    try:
        labels = req_body["labels"]
        result = services.getQuestionsByLabels(labels)
        return HttpResponse(
            json.dumps(result, ensure_ascii=False),
            content_type='application/json')
    except Exception as e:
        print(e)
        return HttpResponse("Bad request")

def getIds(request):
    result = services.getIdListOfQuestions()
    return HttpResponse(
        json.dumps(result, ensure_ascii=False),
        content_type='application/json')

def getAllFinishedQuestions(request):
    result = services.getAllQuestions()
    return HttpResponse(
        json.dumps(result, ensure_ascii=False),
        content_type='application/json')
