# admin.py
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'assigned_to', 'created_by', 'status', 'deadline', 'created_at')  # Add status to the list
    search_fields = ('task_name', 'assigned_to__username', 'created_by__username', 'status')  # Make task name and user searchable
    list_filter = ('assigned_to', 'created_by', 'status', 'deadline')  # Add filters to the admin page
