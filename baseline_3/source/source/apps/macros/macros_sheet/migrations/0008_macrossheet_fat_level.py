# Generated by Django 4.2.1 on 2023-06-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macros_sheet', '0007_macrossheet_ptn_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='macrossheet',
            name='fat_level',
            field=models.CharField(default='is_normal_fat', max_length=20),
        ),
    ]