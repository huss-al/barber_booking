from django.db import models
from profiles.models import Profile
from barbers.models import Barber
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='appointments')
    barber = models.ForeignKey(
        'barbers.barber', on_delete=models.CASCADE, related_name='appointments'
        )
    cut = models.ForeignKey(
        'CutType', on_delete=models.CASCADE, related_name='appointments')
    contact = models.CharField(max_length=20, default='Unknown')

    class Meta:
        unique_together = ('date', 'time', 'barber',)

    def clean(self):
        # Validate that the appt doesn't overlap with existing appt barber
        existing_appointments = Appointment.objects.filter(
            barber=self.barber, date=self.date, time=self.time)
        if self.pk:
            existing_appointments = existing_appointments.exclude(pk=self.pk)
        if existing_appointments.exists():
            raise ValidationError(
                'Barber is unavailable at this time.'
            )

    def __str__(self):
        return (f"Appointment {self.id} for {self.client.user.username} "
                f"with {self.barber.name} on {self.date} at {self.time}")


class CutType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name
