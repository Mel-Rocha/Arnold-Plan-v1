# Generated by Django 5.0 on 2024-08-17 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_info', '0001_initial'),
        ('macros_planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='macros_planner',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='macros_planner.macrosplanner'),
        ),
    ]
