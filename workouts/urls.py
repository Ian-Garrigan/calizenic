from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_app, name='add_workout'),
]

# view should be add workout + name space. Use name for href refer
# urlpatterns = [
#     path('', views.my_app, name='add_workout'),
# ]

