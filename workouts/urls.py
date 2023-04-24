from django.urls import path

from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user-dashboard/', views.UserDashboard.as_view(), name='user-dashboard'),
    path('user-templates-list/', views.UserTemplatesList.as_view(), name='user-templates-list'),
    path('create-workout/', views.create_workout_template, name='create-workout'),
    path('view-logs/<int:id>/', views.view_log, name='view-log'),
    path('edit-log/<int:id>/', views.edit_log, name='edit-log'),
    path('delete-workout-template/<int:id>/', views.delete_workout_template, name='delete-workout-template'),
]
