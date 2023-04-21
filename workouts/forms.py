from django import forms

from .models import *


class DataFromWorkoutTemplate(forms.ModelForm):
    class Meta:
        model = WorkoutTemplate
        fields = ('template_name', )
        labels = {
            'template_name': 'Template Name',
        }


class DataFromWorkoutLogAndExercises(forms.ModelForm):
    exercise_dropdown = forms.ModelChoiceField(
        queryset=Exercises.objects.all(),
        label='Exercise Type',
        required=True,
        empty_label='Choose one:',
        widget=forms.Select(attrs={'id': 'select-exercise'}),
    )

    class Meta:
        model = WorkoutLog
        fields = ('exercise_dropdown', 'weight', 'sets', 'reps', 'note', )
        labels = {
            'weight': 'Weight(Kg)',
            'sets': 'Sets',
            'reps': 'Reps',
            'note': 'Note',
        }
