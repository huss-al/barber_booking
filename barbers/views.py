from django.shortcuts import render, get_object_or_404, redirect
from .models import Barber
from .forms import BarberForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def create_barber(request):
    if request.method == 'POST':
        form = BarberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barber created successfully.')

            return redirect('view_barbers')
    else:
        form = BarberForm()
    return render(request, 'barbers/create_barber.html', {'form': form})


@login_required
def edit_barber(request, id):
    barber = get_object_or_404(Barber, id=id)
    if request.method == 'POST':
        form = BarberForm(request.POST, request.FILES, instance=barber)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barber was updated successfully.')
            return redirect('view_barbers')
    else:
        form = BarberForm(instance=barber)
    return render(
            request,
            'barbers/edit_barber.html', {'form': form, 'barber': barber})


@login_required
def delete_barber(request, id):
    barber = get_object_or_404(Barber, id=id)
    if request.method == 'POST':
        barber.delete()
        messages.success(request, 'Barber deleted successfully.')
        return redirect('view_barbers')
    return render(request, 'barbers/delete_barber.html', {'barber': barber})


@login_required
def view_barbers(request):
    barbers = Barber.objects.all()
    return render(request, 'barbers/view_barbers.html', {'barbers': barbers})
