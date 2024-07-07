from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Gallery, AboutUsContent, ContactMessage, CutType
from .forms import ProfileForm, ContactForm, ContactForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login



# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def services_page(request):
    cut_types = CutType.objects.all()
    return render(request, 'home/services.html', {'cut_types': cut_types})


def gallery(request):
    return render(request, 'home/gallery.html') 

def gallery_view(request):
    images = Gallery.objects.all()  
    return render(request, 'home/gallery.html', {'images': images})


def about_us(request):
    return render(request, 'home/about_us.html')   

def about_us(request):
    content = AboutUsContent.objects.first()  # Assuming there's only one About Us content
    return render(request, 'home/about_us.html', {'content': content})


def contact_us(request):
    return render(request, 'home/contact_us.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            return redirect('contact_us_confirmation')
    else:
        form = ContactForm()

    return render(request, 'home/contact_us.html', {'form': form})



def contact_us_confirmation(request):
    last_message = ContactMessage.objects.last()  # Get the last submitted message
    return render(request, 'home/contact_us_confirmation.html', {'message': last_message})

def booking_page(request):
    return render(request, 'home/booking_page.html')

