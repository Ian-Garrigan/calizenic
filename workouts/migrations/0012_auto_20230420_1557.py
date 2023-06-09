# Generated by Django 3.2.18 on 2023-04-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0011_alter_workouttemplate_template_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutlog',
            name='reps',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='workoutlog',
            name='sets',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='workoutlog',
            name='weight',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
