from django.urls import path

from . import views

urlpatterns = [
    path('add-workout/', views.add_workout, name='workout'),
]
