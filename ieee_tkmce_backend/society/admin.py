from django.contrib import admin

from .models import Society


@admin.register(Society)
class SocietyAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]
