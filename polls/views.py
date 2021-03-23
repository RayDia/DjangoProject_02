from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question, Choice
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404


def index(request):
    question_list = Question.objects.all()[:3]
    #question_list = get_list_or_404(Question, pk=2)
    contex = {'question_list': question_list}
    return render(request, 'polls/index.html', contex)


def detail(request, question_id):
    # try:
    # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    # raise Http404("Error!\n Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "Hello.\n  This is the result of Question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting for Question %s." % question_id)
