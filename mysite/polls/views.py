from django.shortcuts import render
from django.http import HttpResponse


from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:2]

    context = {
        "latest_question_list":latest_question_list,
    }
    return render(request, "polls/index.html" , context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse("You're voitng on question %s." % question_id)