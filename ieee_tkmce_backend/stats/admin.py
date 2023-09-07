from django.contrib import admin

from .models import Stats


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    fields = ("title", "value")  # slug field is avoided , it's value will be generated from save function in the model
    search_fields = ["title"]
    list_display = ["title", "value", "slug"]
