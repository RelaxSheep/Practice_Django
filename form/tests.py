from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question


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
