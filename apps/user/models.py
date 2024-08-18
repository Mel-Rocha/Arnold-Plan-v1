from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator


# Base class for profile
class Gender(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=Gender.choices)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    class Meta:
        abstract = True


# Athlete
class Category(models.TextChoices):
    MENS_PHYSIQUE = 'MENS_PHYSIQUE', 'Mens Physique'
    BODYBUILDER = 'BODYBUILDER', 'Bodybuilder'
    WELLNESS = 'WELLNESS', 'Wellness'
    FIGURE = 'FIGURE', 'Figure'
    FIT_MODEL = 'FIT_MODEL', 'Fit Model'
    NOVICE = 'NOVICE', 'Novice'
    TRUE_NOVICE = 'TRUE_NOVICE', 'True Novice'
    OVERCOMING = 'OVERCOMING', 'Overcoming'


class Athlete(Profile):
    nutritionist = models.ForeignKey(
        'Nutritionist',
        on_delete=models.SET_NULL,
        related_name='athletes',
        null=True,
        blank=True
    )
    category = models.CharField(max_length=50, choices=Category.choices)
    weight = models.FloatField(default=1, validators=[MinValueValidator(1)])
    height = models.FloatField(default=1, validators=[MinValueValidator(1)])
    birth_date = models.DateField()
    is_pro = models.BooleanField(default=False)


# Nutritionist
class AcademicDegree(models.TextChoices):
    BACHELOR = 'BACHELOR', 'Bachelor'
    POSTGRADUATE = 'POSTGRADUATE', 'Postgraduate'
    MASTER = 'MASTER', 'Master'
    DOCTOR = 'DOCTOR', 'Doctor'


class Nutritionist(Profile):
    crn = models.CharField(max_length=255)
    academic_degree = models.CharField(
        max_length=20,
        choices=AcademicDegree.choices,
        default=AcademicDegree.BACHELOR,
    )
    area_of_specialization = models.CharField(max_length=255)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()