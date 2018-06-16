from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Question, Ans

# Create your views here.
def homepage(request):
    ques_all = Question.objects.all()
    return render(request, 'homepage.html', {'ques_all': ques_all})

def vote(request, question_id):
    return render(request, 'vote.html')
