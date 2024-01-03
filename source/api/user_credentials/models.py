from django.db import models
from django.contrib.auth.models import User

class UserCredentials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credentials_json = models.TextField()
