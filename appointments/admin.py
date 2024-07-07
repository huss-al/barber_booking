from django.contrib import admin
from .models import Appointment, CutType

# Register your models here.
from django.contrib import admin
from .models import Appointment, CutType

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime', 'client', 'barber', 'cut')

@admin.register(CutType)
class CutTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'duration')