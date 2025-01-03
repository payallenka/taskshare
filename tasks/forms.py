from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'assigned_to', 'deadline', 'status','report']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the view

        super().__init__(*args, **kwargs)

        # If the user is the assignee, restrict them to only modifying the status field
        if user and self.instance.assigned_to == user:
            self.fields['task_name'].disabled = True
            self.fields['description'].disabled = True
            self.fields['assigned_to'].disabled = True
            self.fields['deadline'].disabled = True
        elif user and self.instance.created_by != user:
            # If the user is neither the assignee nor the creator, disable all fields
            for field in self.fields:
                self.fields[field].disabled = True
