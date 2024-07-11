from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path("accounts/", include("allauth.urls")),
    path('view/', views.view_profile, name='view_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
]
