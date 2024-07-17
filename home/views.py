from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Gallery, AboutUsContent, ContactMessage, CutType
from .forms import (
    ProfileForm, ContactForm, BookingEditForm, AppointmentForm
)
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from appointments.models import Appointment
from django.utils import timezone
from django.db import IntegrityError
from barbers.models import Barber
from django.contrib import messages


# Create your views here.
def home(request):
    gallery_images = Gallery.objects.all()  # Query all gallery images
    barbers = Barber.objects.all()  # Fetch all barbers from the database
    return render(
        request, 'home/home.html',
        {'gallery_images': gallery_images, 'barbers': barbers}
    )


def services_page(request):
    cut_types = CutType.objects.all()
    return render(request, 'home/services.html', {'cut_types': cut_types})


def gallery(request):
    return render(request, 'home/gallery.html')


def gallery_view(request):
    images = Gallery.objects.all()
    return render(request, 'home/gallery.html', {'images': images})


def about_us(request):
    content = AboutUsContent.objects.first()
    return render(request, 'home/about_us.html', {'content': content})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            messages.success(request, 'Your message was sent successfully.')

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
    last_message = ContactMessage.objects.last()
    return render(
        request, 'home/contact_us_confirmation.html',
        {'message': last_message}
    )


@login_required
def user_bookings(request):
    user = request.user
    now = timezone.now()

    upcoming_appointments = Appointment.objects.filter(
        client=user.profile, date__gte=timezone.now()
    ).order_by('date', 'time')
    past_appointments = Appointment.objects.filter(
        client=user.profile, date__lt=timezone.now()
    ).order_by('-date', '-time')
    return render(
        request, 'home/user_bookings.html',
        {
            'upcoming_appointments': upcoming_appointments,
            'past_appointments': past_appointments,
        }
    )


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            try:
                appointment = form.save(commit=False)
                appointment.client = request.user.profile
                appointment.save()
                messages.success(request, 'Your booking was successfully.')
                return redirect(
                    'booking-detail',
                    appointment_id=appointment.id
                )
            except IntegrityError as e:
                form.add_error(
                    None,
                    "Barber unavailable at this date and time."
                )
        else:
            messages.error(
                request,
                'Sorry, the barber is not available at this time.'
            )
    else:
        form = AppointmentForm()

    return render(request, 'home/create_booking.html', {'form': form})


@login_required
def edit_booking(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, id=appointment_id, client=request.user.profile
    )
    if request.method == 'POST':
        form = BookingEditForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your new booking was successful.')
            return redirect('user-bookings')
    else:
        form = BookingEditForm(instance=appointment)

    return render(
        request, 'home/edit_booking.html',
        {'form': form, 'appointment': appointment}
    )


@login_required
def cancel_booking(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, id=appointment_id, client=request.user.profile
    )

    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Your booking was cancelled successfully.')

        return redirect('user-bookings')

    return render(
        request, 'home/cancel_booking.html',
        {'appointment': appointment}
    )


def booking_detail(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, id=appointment_id, client=request.user.profile
    )
    return render(
        request, 'home/booking_detail.html',
        {'appointment': appointment}
    )
