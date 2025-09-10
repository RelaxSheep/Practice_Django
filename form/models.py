from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=255, null=False, blank=False)
    public_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.content
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.public_date <= now


class Choice(models.Model):
    option = models.CharField(max_length=255, null=False, blank=False)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.option


