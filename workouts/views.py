from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.views.generic.detail import SingleObjectMixin

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
    fields = ['log_name', 'exercise_type', 'weight', 'sets', 'reps', 'note']

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Workout template has been created'
        )

        return super().form_valid(form)


class CreateWorkoutDetail(DetailView):
    model = WorkoutLog
    template_name = 'detail-create-workout.html'


class EditView(SingleObjectMixin, FormView):
    model = WorkoutLog
    template_name = 'edit-workout.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=WorkoutLog.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=WorkoutLog.objects.all())
        return super().post(request, *args, **kwargs)
    



def tracker_list(request):
    return render(request, 'workouts/tracker-list.html')
