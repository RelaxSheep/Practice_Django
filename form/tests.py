from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse


# Create your tests here.
class QuestionTest(TestCase):
    def test_was_published_recently_with_future_time(self):
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        question_test = Question(public_date=time)
        self.assertIs(question_test.was_published_recently(), False) #assertIs(a, b): a is b(Check identity)
    
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        question_test = Question(public_date=time)
        self.assertIs(question_test.was_published_recently(), True)

#python manage.py test form

def create_question(content, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(content=content, public_date=time)


class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        future_question = create_question('Future question', days=5)
        url = reverse('form:question_detail_view_url', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        