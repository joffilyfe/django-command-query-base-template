from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from .queries import QuestionQueries
from django.http import Http404
from django.urls import reverse
from .units.register_vote import RegisterVote


def index(request):
    context = {
        "latest_question_list": QuestionQueries.published_recently(),
    }
    return render(request, "polls/index.html", context=context)


def detail(request, question_id):
    try:
        question = QuestionQueries.by_pk(question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = QuestionQueries.by_pk(question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    RegisterVote(choice_id=request.POST["choice"]).execute()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
