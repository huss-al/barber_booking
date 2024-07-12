from django.urls import path, include
from . import views 
from .views import CustomLoginView, register



urlpatterns = [
    path('register/',register, name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path("accounts/", include("allauth.urls")),
    path('view/', views.view_profile, name='view_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
]
