from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='home_profile'
    )
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.surname}"


class CutType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = CloudinaryField('max_length=255')

    def __str__(self):
        return f"Gallery Image {self.id}"


class AboutUsContent(models.Model):
    image = CloudinaryField('image')
    description = models.TextField()

    def __str__(self):
        return "About Us Content"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.subject}'  # Display subject in admin panel
