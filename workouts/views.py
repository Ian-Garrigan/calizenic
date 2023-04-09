from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from .models import *
from .forms import *


# def home(request):
#     return render(request, 'base.html')


def add_workout(request):
    workout_templates = WorkoutTemplate.objects.all()

    if request.method == 'POST':
        form = AddWorkout(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('log_workout'))
    else:
        form = AddWorkout()
        context = {
            'workout_templates': workout_templates, 'form': form
        }
        return render(request, 'workouts/user-dashboard.html', context)


def log_workout(request):
    return render(request, 'workouts/create-workout.html')
