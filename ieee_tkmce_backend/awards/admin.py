from django.contrib import admin

from .models import Award


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    search_fields = ["name", "content"]
    list_display = ["name", "designation", "priority"]
    list_filter = ["name", "pub_date"]
