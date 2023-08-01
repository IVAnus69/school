from django.urls import path
from . import views

urlpatterns = [
    path('', views.math, name='math'),
    path('exercise/<int:exercise_id>/', views.exercise, name='exercise')
]