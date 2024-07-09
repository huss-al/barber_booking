from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Barber(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = models.TextField(default='Please add description') 

    def __str__(self):
        return self.name
