# Generated by Django 3.2.18 on 2023-04-11 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_alter_workoutlog_weight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workouttemplate',
            options={'ordering': ['-time_created']},
        ),
    ]
