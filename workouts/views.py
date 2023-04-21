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
            messages.success(request, 'Your Workout template was created')
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
    queryset = WorkoutTemplate.objects.filter(status=0).order_by('-time_created')
    template_name = 'user-templates-list.html'
    paginate_by = 4


def view_logs(request, id):
    title = get_object_or_404(WorkoutTemplate, id=id)
    logs = WorkoutLog.objects.filter(log_name=id).order_by('-id')[:3]
    template = 'view-logs.html'
    context = {
        'title': title,
        'logs': logs
    }
    return render(request, template, context)


def workout_templates_data(request, id):
    workout_template = get_object_or_404(WorkoutTemplate, id=id)
    logs = WorkoutLog.objects.filter(log_name=id).order_by('-id')[:3]
    template = 'view-logs.html'
    context = {
        'title': title,
        'logs': logs
    }
    return render(request, template, context)
    

    
# Allows for editing and updating of a specific workout template 
# def edit_workout(request, id):
#     workout_template = get_object_or_404(WorkoutTemplate, id=id)
#     workout_log = get_object_or_404(WorkoutLog, log_name=workout_template)

#     if request.method == 'POST':
#         workout_template_form = WorkoutTemplateForm(request.POST, instance=workout_template)
#         workout_log_form = WorkoutLogForm(request.POST, instance=workout_log)
#         if workout_template_form.is_valid() and workout_log_form.is_valid():
#             workout_template_form.save()
#             workout_log_form.save()
#             messages.success(request, 'Your workout template has been updated')
#             return redirect('user-templates-list.html')
#     else:
#         workout_template_form = WorkoutTemplateForm(instance=workout_template)
#         workout_log_form = WorkoutLogForm(instance=workout_log)

#     context = {
#         'workout_template_form': workout_template_form,
#         'workout_log_form': workout_log_form,
#     }

#     return render(request, 'edit-workout.html', context)


def tracker_list(request):
    return render(request, 'workouts/tracker-list.html')
