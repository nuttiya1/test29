from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField(max_length=200)

class Ans(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans_text = models.TextField(max_length=50)
    votes = models.IntegerField(default=0)
