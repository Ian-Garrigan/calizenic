# Generated by Django 3.2.18 on 2023-04-13 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0007_workouttemplate_log_entries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workouttemplate',
            name='log_entries',
        ),
    ]
