from django import forms
from django.forms import inlineformset_factory

from .models import *


WorkoutsFormset = inlineformset_factory(WorkoutTemplate, WorkoutLog, fields=())
 