from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ["name", "contact_number"]
    list_display = ["name", "contact_number"]
