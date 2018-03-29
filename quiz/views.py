from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
     return render(request, 'homepage.html')

def vote(request, question_id):
    return render(request, 'vote.html')
