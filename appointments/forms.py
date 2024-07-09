from django import forms
from .models import Appointment, CutType
from barbers.models import Barber
from datetime import datetime, time, timedelta


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['notes', 'date', 'time', 'client', 'barber', 'cut']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


OPENING_HOURS_START = 9  # 9am
OPENING_HOURS_END = 18   # 6pm

class BookingForm(forms.ModelForm):
    cut = forms.ModelChoiceField(queryset=CutType.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    barber = forms.ModelChoiceField(queryset=Barber.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}))
    time = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Generate time choices in 1-hour intervals
        appointment_time_choices = []
        start_time = datetime.combine(self.initial.get('date', datetime.today().date()), time(9, 0))  # Replace with your opening hour
        end_time = datetime.combine(self.initial.get('date', datetime.today().date()), time(18, 0))  # Replace with your closing hour

        current_time = start_time
        while current_time <= end_time:
            appointment_time_choices.append(
                (current_time.strftime('%H:%M'), current_time.strftime('%I:%M %p'))  # Format for display
            )
            current_time += timedelta(minutes=15)

        self.fields['time'].choices = appointment_time_choices
        # Optionally set initial value for time field
        if appointment_time_choices:
            self.fields['time'].initial = appointment_time_choices[0][0]  # Set initial value to the first choice

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            try:
                datetime_str = f"{date} {time}"
                cleaned_data['date'] = date
                cleaned_data['time'] = time
            except ValueError:
                raise forms.ValidationError("Invalid date/time format.")

        return cleaned_data

    class Meta:
        model = Appointment
        fields = ['cut', 'barber', 'date', 'time', 'contact', 'notes']
        