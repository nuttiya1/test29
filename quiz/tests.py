from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from django.test import Client
from quiz.views import homepage
from quiz.models import Question, Ans

class HomePageTest(TestCase):
    def test_root_hotme_page(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title> Quiz </title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'homepage.html')

    def test_only_save_question_ans_vote(self):
        Question.objects.create( question_text = "1 + 1 = 3 ?")
        q = Question.objects.first()
        self.assertEqual(q.question_text, '1 + 1 = 3 ?')
        self.assertEqual(Question.objects.count(), 1)

        q.ans_set.create(ans_text='True', votes=0)
        q.ans_set.create(ans_text='False', votes=0)
        self.assertEqual(q.ans_set.count(), 2)
