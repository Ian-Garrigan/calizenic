from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Template'), (1, 'Add to Tracker'))


class WorkoutTemplate(models.Model):

    athlete_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='athlete')
    template_name = models.CharField(max_length=50, default='New workout template')
    time_created = models.DateTimeField(auto_now_add=True)
    total_completed = models.PositiveIntegerField(default=0)
    was_performed = models.BooleanField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.template_name


class Exercises(models.Model):

    exercise_name = models.CharField(max_length=50, unique=True)
    exercise_image = CloudinaryField()
    muscle_group = models.CharField(max_length=50)

    def __str__(self):
        return self.exercise_name

    class Meta:
        verbose_name_plural = 'Exercises'


class WorkoutLog(models.Model):

    log_name = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE)
    # exercise_type = models.ForeignKey(Exercises, on_delete=models.CASCADE, to_field='exercise_name')
    weight = models.PositiveIntegerField(default=10)
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(default=5)
    note = models.TextField()


class Tracker(models.Model):

    recent_workouts = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE, related_name='workout')

    def __str__(self):
        return f"{self.recent_workouts.template_name} was recently performed"
    
    class Meta:
        ordering = ['-recent_workouts']
        verbose_name_plural = 'Tracker'
