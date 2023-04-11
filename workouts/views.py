from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (TemplateView, ListView, CreateView)

from .models import *
from .forms import *


class HomeView(TemplateView):
    template_name = 'home.html'


class UserDashboard(TemplateView):
    template_name = 'user-dashboard.html'


class UserTemplatesList(ListView):
    model = WorkoutTemplate
    context_object_name = 'user_templates'
    queryset = WorkoutTemplate.objects.filter(status=0).order_by('-time_created')
    template_name = 'user-templates-list.html'
    paginate_by = 4


class CreateWorkout(CreateView):
    model = WorkoutLog
    context_object_name = 'create_workout'
    template_name = 'create-workout.html'
    fields = ['exercise_type',]

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'{self.log_name} has been created'
        )

        return super().form_valid(form)


# def create_workout(request):
#     return render(request, 'workouts/create-workout.html')
    

# def user_dashboard(request): 
#     return render(request, 'workouts/user-dashboard.html')


# def user_templates_list(request):
#     return render(request, 'workouts/user-templates-list.html')


def tracker_list(request):
    return render(request, 'workouts/tracker-list.html')
