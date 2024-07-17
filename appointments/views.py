from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm, BookingForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Appointment, CutType
from django.contrib import messages
from profiles.models import Profile


@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user.profile
            messages.success(request, 'Your booking was successfully.')
            appointment.save()
            return redirect('show_appointment', appointment_id=appointment.id)
    else:
        form = BookingForm()
    return render(
        request, 'appointments/create_appointment.html', {'form': form}
    )


@login_required
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your new booking was successful.')
            return redirect('show_appointment', appointment_id=appointment.id)
    else:
        form = BookingForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {
        'form': form, 'appointment': appointment})


@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Your booking was cancelled successfully.')
        return redirect('show_all_appointment')
    return render(request, 'appointments/delete_appointment.html', {
        'appointment': appointment})


@login_required
def show_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'appointments/show_appointment.html', {
        'appointment': appointment})


@login_required
def show_all_appointment(request):
    appointments = Appointment.objects.filter(client=request.user.profile)
    return render(request, 'appointments/show_all_appointment.html', {
        'appointments': appointments})


@staff_member_required
def admin_create_cut(request):
    # Implementation for admin to create CutType objects
    pass


@staff_member_required
def admin_edit_cut(request, cut_id):
    # Implementation for admin to edit CutType objects
    pass


@staff_member_required
def admin_delete_cut(request, cut_id):
    # Implementation for admin to delete CutType objects
    pass


@staff_member_required
def admin_view_all_cuts(request):
    cuts = CutType.objects.all()
    return render(
        request, 'appointments/admin_view_all_cuts.html', {'cuts': cuts}
    )


@staff_member_required
def admin_view_cut(request, cut_id):
    cut = get_object_or_404(CutType, pk=cut_id)
    return render(request, 'appointments/admin_view_cut.html', {'cut': cut})


@login_required
def booking_page(request):
    booking_not_available = False

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            appointment_date = form.cleaned_data['date']
            appointment_time = form.cleaned_data['time']
            barber = form.cleaned_data['barber']

            if not is_booking_available(
                appointment_date, appointment_time, barber
            ):
                booking_not_available = True
                messages.error(
                    request, 'The barber is not available at this time.'
                )
            else:
                try:
                    profile = request.user.profile
                except Profile.DoesNotExist:
                    profile = Profile.objects.create(user=request.user)

                appointment = form.save(commit=False)
                appointment.client = profile
                appointment.save()
                messages.success(request, 'Your booking was successful.')
                return redirect(
                    'booking-success', appointment_id=appointment.pk
                )
    else:
        form = BookingForm()

    return render(request, 'home/booking_page.html', {
        'form': form, 'booking_not_available': booking_not_available})


def is_booking_available(appointment_date, appointment_time, barber):
    existing_appointments = Appointment.objects.filter(
        date=appointment_date, time=appointment_time, barber=barber)
    return not existing_appointments.exists()


@login_required
def booking_success(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(
        request, 'home/booking_success.html', {'appointment': appointment}
    )
