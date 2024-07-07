from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Check if the instance is not a superuser
        if not instance.is_superuser:
            Profile.objects.create(user=instance)
    else:
        # Handle update case here if necessary
        pass
