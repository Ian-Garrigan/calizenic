# Generated by Django 3.2.18 on 2023-04-13 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0006_alter_exercises_exercise_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouttemplate',
            name='log_entries',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workouts.workoutlog'),
        ),
    ]
