from django import forms

from .models import *


class CreateWorkoutTemplateForm(forms.Form):
    template_name = forms.CharField(
        label='Template Name',
        max_length=50,
        )
    exercise = forms.ModelChoiceField(
        queryset=Exercises.objects.all(),
        widget=forms.Select(attrs={'id': 'exercise-select'}),
        )
    muscle_group = forms.CharField(
        label='Muscle Group',
        max_length=50,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
    )
    weight = forms.DecimalField(
        label='Weight(Kg)',
        max_digits=3,
        decimal_places=1,
        initial=00.0,
    )
    sets = forms.IntegerField(
        label='Number of Sets',
        initial=3,
    )
    reps = forms.IntegerField(
        label='Number of Reps',
        initial=5,
    )
    note = forms.Textarea(
        attrs={'rows': 6},
        label='Note',
        required=False,
        initial='You can include any additional notes or comments about your workout here, '
                'such as modifications you made to the routine or reminders for future sessions.',
    )


# class CreateWorkoutForm(forms.ModelForm):
#     class Meta:
#         model = WorkoutLog
#         exclude = ('log_name', )
#         labels = {
#             # 'log_name': 'Template Name',
#             'weight': 'Weight(Kg)',
#             'sets': 'Number of Sets',
#             'reps': 'Number of Reps',
#             'note': 'Workout Note',
#         }
#         widgets = {
#         'note': forms.Textarea(attrs={'rows': 6}),
#         }



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
