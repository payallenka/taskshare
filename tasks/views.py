from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required

# View to list tasks
def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# View to create a new task
def task_create(request):
    users = User.objects.all()  # Fetch all users from the database to display in the dropdown
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save to the database yet
            task.created_by = request.user  # Set the logged-in user as the creator of the task
            task.save()  # Save the task to the database
            return redirect('tasks:task_list')  # Redirect to the task list page after saving
    else:
        form = TaskForm()

    # Render the form in the template and pass the users to the dropdown
    return render(request, 'tasks/task_create.html', {'form': form, 'users': users})



@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Get the task to edit
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)  # Pass user to form
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('tasks:task_list')  # Correct reference to the task list view
    else:
        form = TaskForm(instance=task, user=request.user)  # Pass user to form

    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})


# View to delete a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:task_list')  # Redirect to the task list after deletion

@api_view(['GET'])
@login_required
def user_tasks_api(request):
    tasks = Task.objects.filter(assigned_to=request.user)  # Filter tasks for the logged-in user
    serializer = TaskSerializer(tasks, many=True)  # Serialize the tasks
    return Response(serializer.data)  # Return JSON response