# Generated by Django 4.2.1 on 2023-12-24 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Diet',
            new_name='Meal',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='Diet',
            new_name='diet',
        ),
    ]