from django import forms
from django.forms import ModelForm

from .models import *


class AddWorkout(forms.ModelForm):

    class Meta:
        model = WorkoutTemplate
        fields = ['template_name', 'was_performed', ]
