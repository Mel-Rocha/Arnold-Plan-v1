# Generated by Django 5.1 on 2024-08-18 11:46

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutritionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('crn', models.CharField(max_length=255)),
                ('academic_degree', models.CharField(choices=[('BACHELOR', 'Bachelor'), ('POSTGRADUATE', 'Postgraduate'), ('MASTER', 'Master'), ('DOCTOR', 'Doctor')], default='BACHELOR', max_length=20)),
                ('area_of_specialization', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('MENS_PHYSIQUE', 'Mens Physique'), ('BODYBUILDER', 'Bodybuilder'), ('WELLNESS', 'Wellness'), ('FIGURE', 'Figure'), ('FIT_MODEL', 'Fit Model'), ('NOVICE', 'Novice'), ('TRUE_NOVICE', 'True Novice'), ('OVERCOMING', 'Overcoming')], max_length=50)),
                ('weight', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('height', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('birth_date', models.DateField()),
                ('is_pro', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nutritionist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='athletes', to='user.nutritionist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]