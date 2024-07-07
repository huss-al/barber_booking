from django.db import models
from profiles.models import Profile
from barbers.models import Barber
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField()
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='appointments')
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='appointments')
    cut = models.ForeignKey('CutType', on_delete=models.CASCADE, related_name='appointments')

    class Meta:
        unique_together = ('datetime', 'barber',)

    def clean(self):
        # Validate that the appointment datetime doesn't overlap with existing appointments for the same barber
        existing_appointments = Appointment.objects.filter(barber=self.barber, datetime=self.datetime)
        if self.pk:
            existing_appointments = existing_appointments.exclude(pk=self.pk)
        if existing_appointments.exists():
            raise ValidationError('An appointment already exists with this barber at the specified time.')

    def __str__(self):
        return f"Appointment {self.id} for {self.client.user.username} with {self.barber.user.username} on {self.datetime}"


class CutType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name