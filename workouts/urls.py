from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_app, name='hello'),
]
