from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='tasks'),
    path('add/', views.add_task, name='add_task'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('profile/', views.profile, name='profile'),
    path('contacts/', views.contacts, name='contacts'),
    path('complete/<int:pk>/', views.complete_task, name='complete_task'),
    path('register/', views.register, name='register'),
]