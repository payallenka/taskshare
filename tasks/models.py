# models.py
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True) 
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    report = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.task_name} (Status: {self.status}, Assigned to: {self.assigned_to})"
    
    def is_completed(self):
        return self.status == 'completed'
    
    class Meta:
        ordering = ['-created_at']