
from django.contrib import admin
from .models import Profile, Gallery, AboutUsContent, ContactMessage, CutType
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'surname')


@admin.register(CutType)
class CutTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ('name',)
    list_filter = ('price', 'duration')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')



admin.site.register(AboutUsContent)



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject', 'message')