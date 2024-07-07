from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.user.username