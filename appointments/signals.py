# appointments/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Appointment

@receiver(post_save, sender=Appointment)
def send_appointment_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Appointment Booked'
        message = f'A new appointment has been booked by {instance.client.user.username}.\n\nDetails:\nCut Type: {instance.cut}\nBarber: {instance.barber}\nDate and Time: {instance.datetime}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL]
        send_mail(subject, message, from_email, recipient_list)
