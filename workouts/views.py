from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import *


@login_required
def add_workout(request):
    workout_templates = WorkoutTemplate.objects.all()

    if request.method == 'POST':
        initial_data = {'athlete_id': request.user.id}
        form = AddWorkout(request.POST, initial=initial_data)
        if form.is_valid():
            form.save()
            return redirect(reverse('log_workout'))
    else:
        initial_data = {'athlete_id': request.user.id}
        form = AddWorkout(request.user, initial=initial_data)
        context = {
            'workout_templates': workout_templates, 'form': form
        }
        return render(request, 'workouts/user-dashboard.html', context)


def log_workout(request):
    return render(request, 'workouts/create-workout.html')


def home(request):
    return render(request, 'base.html')