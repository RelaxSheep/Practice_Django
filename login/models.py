from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    class GenderChoice(models.IntegerChoices):
        MALE = 0, 'Male'
        FEMALE = 1, 'Female'
        NOT_DEFINED = 2, 'Not defined'
    gender = models.IntegerField(choices=GenderChoice.choices, default=GenderChoice.MALE)
    age = models.IntegerField(default=0)
    