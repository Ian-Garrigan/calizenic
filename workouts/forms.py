from django import forms

from .models import *


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        exclude = ()
        labels = {
            'log_name': 'Template Name',
            'weight': 'Weight(Kg)',
            'sets': 'Number of Sets',
            'reps': 'Number of Reps',
            'note': 'Workout Note',
        }


class WorkoutTemplateForm(forms.ModelForm):
    class Meta:
        model = WorkoutTemplate
        fields = ('template_name', 'status')
        labels = { 
            'template name': 'Template Name',
            'status': 'Status',
        }


class WorkoutLogForm(forms.ModelForm):
    exercise_type = forms.ModelChoiceField(
        queryset=Exercises.objects.all(),
        label='Exercise Type',
        required=True,
        empty_label='Choose Exercise',
    )

    class Meta:
        model = WorkoutLog
        fields = ('exercise_type', 'weight', 'sets', 'reps', 'note')
        labels = {
            'weight': 'Weight',
            'sets': 'Sets',
            'reps': 'Reps',
            'note': 'Note',
        }
