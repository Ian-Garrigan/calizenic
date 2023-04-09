from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *


def add_workout(request):
    workout_templates = WorkoutTemplate.objects.all()

    form = AddWorkout()
    context = {
        'workout_templates': workout_templates, 'form': form
    }
    return render(request, 'workouts/user-dashboard.html', context)


# def home(request):
#     return render(request, 'base.html')
