from django import forms
from .models import *


class DataFromWorkoutTemplate(forms.ModelForm):
    class Meta:
        model = WorkoutTemplate
        fields = ('template_name', )
        labels = {
            'template_name': 'Template Name',
        }

    def __init__(self, *args, **kwargs):
        super(DataFromWorkoutTemplate, self).__init__(*args, **kwargs)
        self.fields['template_name'].widget.attrs['placeholder'] = ' (e.g. Bicep Bonanza)'


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

    def __init__(self, *args, **kwargs):
        super(DataFromWorkoutLogAndExercises, self).__init__(*args, **kwargs)
        self.fields['note'].widget.attrs['placeholder'] = 'e.g. Focus on your breathing and engage your core.'
        self.fields['reps'].initial = 0
        self.fields['sets'].initial = 0
        self.fields['weight'].initial = 5.0


class EditLogForm(forms.ModelForm):
   
    class Meta:
        model = WorkoutLog
        fields = ('exercise_type', 'weight', 'sets', 'reps', 'note' )

    def save(self, commit=True):
        log = super(EditLogForm, self).save(commit=False)
        log.exercise_dropdown = self.cleaned_data['exercise_type']
        if commit:
            log.save()
        return log
