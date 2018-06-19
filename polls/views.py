from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    #output = ', '.join([q.question_text for q in latest_question_list])
    #   output = output +  "<P>DAWGS</P><img src='turkey.jpg'>"
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

 #   return HttpResponse("Les Turkeys s'amusient, et vous, vous vous amusiez?")

