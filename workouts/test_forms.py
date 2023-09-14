from django.test import TestCase
from .forms import DataFromWorkoutTemplate, DataFromWorkoutLogAndExercises


class TestDataFromWorkoutTemplate(TestCase):

    def test_template_name_field_required(self):
        form = DataFromWorkoutTemplate({
            'template_name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('template_name', form.errors.keys())
        self.assertEqual(form.errors['template_name'][0], 'This field is required.')


    def test_form_metaclass_name_relation(self):
        form = DataFromWorkoutTemplate()
        self.assertEqual(form.Meta.fields, ('template_name', ))


class TestDataFromWorkoutLogAndExercises(TestCase):

    def test_fields_are_required(self):
        form = DataFromWorkoutLogAndExercises({
            'sets': 0,
            'reps': 0,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('sets', form.errors.keys())
        self.assertIn('reps', form.errors.keys())
        self.assertEqual(form.errors['sets'][0], 'This field is required.')
        self.assertEqual(form.errors['reps'][0], 'This field is required.')

    def test_fields_are_not_required(self):
        form = DataFromWorkoutLogAndExercises({
            'weight': ''
        })
        self.assertTrue(form.is_valid())


    def test_fields_are_from_form_metaclass(self):
        form = DataFromWorkoutLogAndExercises()
        self.assertEqual(form.Meta.fields, ('exercise_dropdown', 'weight', 'sets', 'reps', 'note', ))


