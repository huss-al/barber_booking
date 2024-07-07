from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_appointment, name='create_appointment'),
    path('edit/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('<int:appointment_id>/', views.show_appointment, name='show_appointment'),
    path('show_all/', views.show_all_appointment, name='show_all_appointment'),
    path('admin/create_cut/', views.admin_create_cut, name='admin_create_cut'),
    path('admin/edit_cut/<int:cut_id>/', views.admin_edit_cut, name='admin_edit_cut'),
    path('admin/delete_cut/<int:cut_id>/', views.admin_delete_cut, name='admin_delete_cut'),
    path('admin/view_all_cuts/', views.admin_view_all_cuts, name='admin_view_all_cuts'),
    path('admin/view_cut/<int:cut_id>/', views.admin_view_cut, name='admin_view_cut'),
    path('booking/', views.booking_page, name='booking-page'),
    path('booking-success/<int:appointment_id>/', views.booking_success, name='booking-success'),
]
