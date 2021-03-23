from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Ray ,this is first app - polls")

def detail(request, question_id):
    return HttpResponse("Hello.\n  This is Question %s." % question_id)

def results(request, question_id):
    response = "Hello.\n  This is the result of Question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for Question %s." % question_id)
