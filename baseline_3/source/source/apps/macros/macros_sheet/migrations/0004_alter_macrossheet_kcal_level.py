# Generated by Django 4.2.1 on 2023-06-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macros_sheet', '0003_macrossheet_kcal_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macrossheet',
            name='kcal_level',
            field=models.CharField(default='is_normal_kcal', max_length=20),
        ),
    ]