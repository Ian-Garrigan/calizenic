# Generated by Django 3.2.18 on 2023-04-05 23:23

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=50)),
                ('exercise_image', cloudinary.models.CloudinaryField(max_length=255)),
                ('muscle_group', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(default='New workout template', max_length=50)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('total_completed', models.PositiveIntegerField(default=0)),
                ('was_performed', models.BooleanField()),
                ('status', models.IntegerField(choices=[(0, 'Template'), (1, 'Added to performed workouts tracker')], default=0)),
                ('athlete_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athlete', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(default=10)),
                ('sets', models.PositiveIntegerField(default=3)),
                ('reps', models.PositiveIntegerField(default=5)),
                ('note', models.TextField()),
                ('log_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workouttemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recent_workouts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workouttemplate')),
            ],
            options={
                'ordering': ['-recent_workouts'],
            },
        ),
    ]
