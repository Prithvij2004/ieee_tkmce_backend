from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ["name", "subject", "email"]
    list_display = ["name", "email", "subject"]
