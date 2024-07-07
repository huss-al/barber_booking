from django.urls import path
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home-page'),
    path('services/', views.services_page, name='services-page'),
    path('gallery/', views.gallery_view, name='gallery-page'),
    path('about_us/', views.about_us, name='about_us-page'),
    path('contact_us/', views.contact_us, name='contact_us-page'),
    path('contact_us/confirmation/', views.contact_us_confirmation, name='contact_us_confirmation'),
    path('booking/', views.booking_page, name='booking-page'),
]