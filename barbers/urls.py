from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_barber, name='create_barber'),
    path('edit/<int:id>/', views.edit_barber, name='edit_barber'),
    path('delete/<int:id>/', views.delete_barber, name='delete_barber'),
    path('', views.view_barbers, name='view_barbers'),
]
