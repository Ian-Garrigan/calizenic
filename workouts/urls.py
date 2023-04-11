from django.urls import path

from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('user-dashboard/', views.UserDashboard.as_view(), name='workouts'),
    path('user-templates-list/', views.UserTemplatesList.as_view(), name='user-templates'),
    path('create-workout/', views.create_workout, name='create-workout'),
    path('tracker-list/', views.tracker_list, name='tracker'),
]