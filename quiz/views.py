from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Question, Ans

# Create your views here.
def homepage(request):
    ques_all = Question.objects.all()
    return render(request, 'homepage.html', {'ques_all': ques_all})

def vote(request):
    question = Question.objects.get(pk=2)
    try:
        selected_answer = question.ans_set.get(pk=request.POST['answer'])
    except (KeyError, Ans.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'vote.html', {'question': question})
    else:
        selected_answer.votes += 1
        selected_answer.save()
    return render(request, 'vote.html', {'question': question})
