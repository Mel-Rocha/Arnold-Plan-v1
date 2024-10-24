# Generated by Django 5.0.8 on 2024-08-10 23:53

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meal', '0002_rename_diet_meal_rename_diet_meal_diet'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealGeneralInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.TimeField(default=datetime.time(0, 0))),
                ('type_of_meal', models.CharField(choices=[('Ordinary', 'Ordinary'), ('Free Meal', 'Free Meal'), ('Pre Workout', 'Pre Workout'), ('Post Workout', 'Post Workout')], default='Ordinary', max_length=50)),
                ('meal', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='meal.meal')),
            ],
        ),
    ]
