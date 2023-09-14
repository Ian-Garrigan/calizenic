from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):

    # def test_get_home_page_renders(self):
    #     response = self.client.get('')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'workouts/home.html')


    def test_get_user_dashboard_renders(self):
        response = self.client.get('/user-dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/workspace/calizenic/workouts/templates/user-dashboard.html')
