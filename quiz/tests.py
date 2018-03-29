from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
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

    def test_user_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Question.objects.count(), 0)

#    def test_can_save_vote(self):
