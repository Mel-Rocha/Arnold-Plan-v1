# Generated by Django 4.2.1 on 2023-12-24 21:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietGeneralInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(blank=True, max_length=100)),
                ('observations', models.CharField(blank=True, max_length=300)),
                ('initial_date', models.DateField()),
                ('final_date', models.DateField()),
                ('weeks', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('type_of_diet', models.CharField(choices=[('Maintenance', 'Maintenance'), ('Bulking', 'Bulking'), ('Cutting', 'Cutting')], max_length=50)),
                ('diet', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='diet.diet')),
            ],
        ),
    ]