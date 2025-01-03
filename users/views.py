from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required


# Register a new user
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            
            # Create a profile instance for the user
            Profile.objects.create(user=user)  # Create a profile after user is saved

            # Success message
            messages.success(request, "Your account has been created successfully!")
            
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html', {'profile': request.user.profile})



@login_required  # Ensures only logged-in users can access this view
def profile(request):
    user = request.user  # Get the logged-in user

    # Check if the user has a profile. If not, we can create one or handle accordingly.
    if hasattr(user, 'profile'):
        organization = user.profile.organization  # Access profile info like organization
    else:
        organization = 'No organization'

    # Prepare context data for rendering
    context = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'organization': organization,
    }
    
    return render(request, 'users/profile.html', context)