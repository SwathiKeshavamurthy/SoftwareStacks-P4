from django.contrib import admin
from .models import About
from .models import About, ContactRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)