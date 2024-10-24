# Generated by Django 5.0 on 2024-08-10 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macros_planner', '0001_initial'),
        ('macros_sheet', '0002_alter_macrossheet_macros_planner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macrossheet',
            name='macros_planner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='macrossheets', to='macros_planner.macrosplanner'),
        ),
    ]
