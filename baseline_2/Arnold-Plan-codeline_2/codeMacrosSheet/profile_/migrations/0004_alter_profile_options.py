# Generated by Django 4.2.2 on 2023-06-27 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0003_alter_profile_height_alter_profile_weight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': True, 'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
    ]