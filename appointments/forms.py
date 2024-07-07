from django import forms
from .models import Appointment, CutType
from barbers.models import Barber


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['notes', 'datetime', 'client', 'barber', 'cut']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class BookingForm(forms.ModelForm):
    cut = forms.ModelChoiceField(queryset=CutType.objects.all())
    barber = forms.ModelChoiceField(queryset=Barber.objects.all())

    class Meta:
        model = Appointment
        fields = ['datetime', 'cut', 'barber', 'contact', 'notes']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    