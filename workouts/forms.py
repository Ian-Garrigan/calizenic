from django import forms
from django.forms import ModelForm

from .models import *


class AddWorkout(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(AddWorkout, self).__init__(*args, **kwargs)
        self.fields['athlete_id'].initial = user.id

    class Meta:
        model = WorkoutTemplate
        fields = ['template_name', 'was_performed', 'athlete_id']


class LogWorkout(forms.ModelForm):

    class Meta:
        model = WorkoutLog
        fields = '__all__'
