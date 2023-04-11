from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (TemplateView, ListView)

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
    paginate_by = 2



# def user_dashboard(request): 
#     return render(request, 'workouts/user-dashboard.html')


# def user_templates_list(request):
#     return render(request, 'workouts/user-templates-list.html')


def create_workout(request):
    return render(request, 'workouts/create-workout.html')


def tracker_list(request):
    return render(request, 'workouts/tracker-list.html')
