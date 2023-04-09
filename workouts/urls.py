from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('add-workout/', views.add_workout, name='workout'),
    path('create-workout/', views.log_workout, name='logworkout'),
]
