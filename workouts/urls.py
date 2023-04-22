from django.urls import path

from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user-dashboard/', views.UserDashboard.as_view(), name='user-dashboard'),
    path('user-templates-list/', views.UserTemplatesList.as_view(), name='user-templates-list'),
    path('create-workout/', views.create_workout_template, name='create-workout'),
    # path('create-workout/<int:pk>/', views.CreateWorkoutDetail.as_view(), name='detail-create-workout'),
    # path('edit-workout/<int:id>', views.edit_workout, name='edit-workout'),
    path('view-logs/<int:id>/', views.view_logs, name='view-logs'),
    path('tracker-list/', views.tracker_list, name='tracker'),
]
