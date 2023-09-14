from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):

    def test_get_home_page_renders(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_get_user_dashboard_renders(self):
        # reverse function to get the url
        url = reverse('workouts:user-dashboard')
        response = self.client.get(url, follow=True) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-dashboard.html')
