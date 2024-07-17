from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from allauth.account.views import LoginView
from allauth.account.forms import LoginForm
from django.contrib.auth.models import User
from django.views import View
from django import forms


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log in the user after registration
            messages.success(
                    request,
                    'Registration successful! You can now book appointments.')
            return redirect('booking-page')
        else:
            messages.error(request, 'Please correct the errors.')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                    "A user with that email already exists.")
        return email


class CustomSignupView(View):
    form_class = CustomUserCreationForm
    template_name = 'account/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log in the user after registration
            messages.success(
                request,
                'Registration successful! You can now book appointments.')
            return redirect('booking-page')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            messages.error(request, 'Please correct the errors.')
        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_invalid(self, form):
        messages.warning(
            self.request, 'Invalid login credentials or unregistered account.')
        return super().form_invalid(form)


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
        return redirect('home')
    return render(request, 'profiles/delete_profile.html')
