# tasks/urls.py
from django.urls import path
from . import views

app_name = 'tasks'  # Set the app_name to 'tasks' so that we can use the 'tasks' namespace

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL for task list
    path('create/', views.task_create, name='task_create'),  # URL for task creation
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),  # URL for editing a task
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),  # URL for deleting a task
    path('api/', views.user_tasks_api, name='user_tasks_api'), 
]
