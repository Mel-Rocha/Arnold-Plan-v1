from django.db import models

from apps.user.profile_.models import Profile

class DailyRecords(models.Model):
    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    date = models.DateField()

    # Refeições
    morning_meal = models.BooleanField(default=False)
    afternoon_meal = models.BooleanField(default=False)
    evening_meal = models.BooleanField(default=False)

    # Hábitos intestinais
    bowel_movements = models.IntegerField(default=0)

    # Horários de fome, estresse, ansiedade e vontade de comer
    hunger_times = models.CharField(max_length=10, choices=TIME_CHOICES, blank=True)
    stress_times = models.CharField(max_length=10, choices=TIME_CHOICES, blank=True)
    anxiety_times = models.CharField(max_length=10, choices=TIME_CHOICES, blank=True)
    craving_times = models.CharField(max_length=10, choices=TIME_CHOICES, blank=True)