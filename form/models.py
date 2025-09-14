from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=255, null=False, blank=False)
    public_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.content
    
    @admin.display( #Decorator cho ham 
        boolean=True, #Hien thi icon thay vi text
        ordering='public_date', #Sap xep theo public_date
        description="Published recently?",  #Header cot
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.public_date <= now


class Choice(models.Model):
    option = models.CharField(max_length=255, null=False, blank=False)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.option

    @admin.display(
        boolean=True,
        description='Has many votes?'   
    )
    def has_many_votes(self):
        return 1 < self.vote
    

