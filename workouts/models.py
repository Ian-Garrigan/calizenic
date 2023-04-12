from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# This will allow the 'workout template' to remain as a draft mock up
# or if performed it'll be sent to the tracker
STATUS = ((0, 'Template'), (1, 'Add to Tracker'))


# Represents the model which allows athletes to set up
# their own workout template and reuse it multiple times.
class WorkoutTemplate(models.Model):

    athlete_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='athlete')
    template_name = models.CharField(max_length=50, default='New workout template')
    time_created = models.DateTimeField(auto_now_add=True)
    total_completed = models.PositiveIntegerField(default=0)
    was_performed = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.template_name


# Model for storing the range of different exercises and
# their associated image, specialized for calisthenics athletes.
class Exercises(models.Model):

    exercise_name = models.CharField(max_length=50)
    exercise_image = CloudinaryField('image', blank=True)
    muscle_group = models.CharField(max_length=50)

    def __str__(self):
        return self.exercise_name

    class Meta:
        verbose_name_plural = 'Exercises'


# A model for storing more precise details about the workout & also allows
# a note input for additional context.
class WorkoutLog(models.Model):

    log_name = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE)
    exercise_type = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    weight = models.DecimalField(default=10.0, max_digits=3, decimal_places=1)
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(default=5)
    note = models.TextField()

    def get_absolute_url(self):
        return reverse('workouts:detail-create-workout', kwargs={'pk': self.pk})

    def __str__(self):
        return self.log_name.template_name


# Model for tracking recently performed workout templates.
# The most recent workouts are displayed at the top of the list
# and the ordering can be modified by changing the 'ordering' attribute of the Meta class.
class Tracker(models.Model):

    recent_workouts = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE, related_name='workout')

    def __str__(self):
        return f"{self.recent_workouts.template_name} was recently performed"

    class Meta:
        ordering = ['-recent_workouts']
        verbose_name_plural = 'Tracker'
