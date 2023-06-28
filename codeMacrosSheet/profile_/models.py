from django.db import models
from enum import Enum
from django.contrib.auth.models import User

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    birth_date =  models.DateField()
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    gender = models.CharField(max_length=50, choices=[(gender.value, gender.name) for gender in Gender])
    

    def __str__(self):
        return self.user.username
    
    