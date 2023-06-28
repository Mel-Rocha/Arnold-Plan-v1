# Generated by Django 4.2.1 on 2023-06-28 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('macros_planner', '0002_macrosplanner_profile'),
        ('macros_sheet', '0009_macrossheet_cho_proportion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='macrossheet',
            name='macros_planner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='macros_planner.macrosplanner'),
        ),
    ]
