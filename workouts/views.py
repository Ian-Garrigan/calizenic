from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)

from .models import *
from .forms import *


class HomeView(TemplateView):
    template_name = 'home.html'


class UserDashboard(TemplateView):
    template_name = 'user-dashboard.html'

# View a list of all the templates a user can choose to use and mark
# as complete(send to tracker)
class UserTemplatesList(ListView):
    model = WorkoutTemplate
    context_object_name = 'user_templates'
    queryset = WorkoutTemplate.objects.filter(status=0).order_by('-time_created')
    template_name = 'user-templates-list.html'
    paginate_by = 4

# Form for creating workout template and display a confirmation message
class CreateWorkout(CreateView):
    model = WorkoutLog
    context_object_name = 'create_workout'
    template_name = 'create-workout.html'
    fields = ['log_name', 'exercise_type', 'weight', 'sets', 'reps', 'note']

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Workout template has been created'
        )

        return super().form_valid(form)


# View the log entries associated with a workout template
# and update,edit, delete them inside a single form
class CreateWorkoutDetail(DetailView):
    model = WorkoutLog
    template_name = 'detail-create-workout.html'


def view_logs(request, id):
    title = get_object_or_404(WorkoutTemplate, id=id)
    logs = WorkoutLog.objects.filter(log_name=id).order_by('-id')[:3]
    template = 'view-logs.html'
    context = {
        'title': title,
        'logs': logs
    }
    return render(request, template, context)


# Allows for editing and updating of a specific workout template 
def edit_workout(request, id):
    workout_template = get_object_or_404(WorkoutTemplate, id=id)
    workout_log = get_object_or_404(WorkoutLog, log_name=workout_template)

    if request.method == 'POST':
        workout_template_form = WorkoutTemplateForm(request.POST, instance=workout_template)
        workout_log_form = WorkoutLogForm(request.POST, instance=workout_log)
        if workout_template_form.is_valid() and workout_log_form.is_valid():
            workout_template_form.save()
            workout_log_form.save()
            messages.success(request, 'Your workout template has been updated')
            return redirect('user-templates-list.html')
    else:
        workout_template_form = WorkoutTemplateForm(instance=workout_template)
        workout_log_form = WorkoutLogForm(instance=workout_log)

    context = {
        'workout_template_form': workout_template_form,
        'workout_log_form': workout_log_form,
    }

    return render(request, 'edit-workout.html', context)


def tracker_list(request):
    return render(request, 'workouts/tracker-list.html')
