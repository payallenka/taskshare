from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user

            # Create a profile instance for the user
            Profile.objects.create(user=user)

            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html', {'profile': request.user.profile})


@login_required  # Ensures only logged-in users can access this view
def profile(request):
    user = request.user  # Get the logged-in user
    context = {
        'username': user.username,  
        'email': user.email,  
        'first_name': user.first_name,
        'last_name': user.last_name,
        'organization': user.profile.organization if hasattr(user, 'profile') else 'No organization',  # Fetch additional info if profile exists
    }
    return render(request, 'users/profile.html', context)