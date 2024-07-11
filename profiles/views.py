from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log in the user after registration
            messages.success(request, 'Registration successful! You can now book appointments.')
            return redirect('booking-page')  # Redirect to 'user-bookings' after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'account/signup.html', {'form': form})


@login_required
def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profiles/view_profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profiles/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('home')  # Replace 'home' with the URL name of your home page
    return render(request, 'profiles/delete_profile.html')