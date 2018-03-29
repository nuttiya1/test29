from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from quiz.views import homepage
from quiz.models import Question, Ans

class HomePageTest(TestCase):
    def test_user_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Question.objects.count(), 0)
