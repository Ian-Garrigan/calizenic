# Generated by Django 3.2.18 on 2023-04-11 22:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_alter_workouttemplate_was_performed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='exercise_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]