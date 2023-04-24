from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (TemplateView, ListView)

from .models import *
from .forms import *


class HomeView(TemplateView):
    template_name = 'home.html'


class UserDashboard(TemplateView):
    template_name = 'user-dashboard.html'


@login_required
def create_workout_template(request):
    context = {}
    if request.method == 'POST':
        workout_name = DataFromWorkoutTemplate(request.POST)
        workout_entries = DataFromWorkoutLogAndExercises(request.POST)
        if workout_name.is_valid() and workout_entries.is_valid():
            workout_name_instance = workout_name.save(commit=False)
            workout_name_instance.athlete_instance = request.user
            workout_name_instance.save()
            workout_entries_instance = workout_entries.save(commit=False)
            workout_entries_instance.log_name = workout_name_instance
            workout_entries_instance.exercise_type = workout_entries.cleaned_data['exercise_dropdown']
            workout_entries_instance.save()
            messages.success(request, 'Your workout template was created')
            return redirect('workouts:create-workout')
        else:
            messages.error(request, 'An error occurred, please try again')
            print(workout_name.errors)
            print(workout_entries.errors)
    else:
        workout_name = DataFromWorkoutTemplate()
        workout_entries = DataFromWorkoutLogAndExercises()
        context = {
            'form1': workout_name,
            'form2': workout_entries
        }
    return render(request, 'create-workout.html', context)


class UserTemplatesList(ListView):
    model = WorkoutTemplate
    context_object_name = 'user_templates'
    queryset = WorkoutTemplate.objects.all().order_by('-time_created')
    template_name = 'user-templates-list.html'
    paginate_by = 6


def view_log(request, id):
    title = get_object_or_404(WorkoutTemplate, id=id)
    logs = WorkoutLog.objects.filter(log_name=id).order_by('-id')[:3]
    template = 'view-logs.html'
    context = {
        'title': title,
        'logs': logs
    }
    return render(request, template, context)


@login_required
def edit_log(request, id):
    log = get_object_or_404(WorkoutLog, id=id)

    if request.method == 'POST':
        edit_form = EditLogForm(request.POST, instance=log)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Log entry updated')
            return redirect('workouts:view_log', id=log.log_name.id)
        else:
            messages.error(request, 'An error occurred, please try again')
    else:
        edit_form = EditLogForm(instance=log)

    context = {
        'edit_form': edit_form
    }
    return render(request, 'edit-log.html', context)