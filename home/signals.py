from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from home.models import Profile  # Adjust based on where your Profile model is located

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Create a profile only if the user is not a superuser
        if not instance.is_superuser:
            Profile.objects.create(user=instance)
