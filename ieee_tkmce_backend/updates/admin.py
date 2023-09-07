from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedTabularInline

from .models import Event, Image


class ImageTabularInline(NestedTabularInline):
    model = Image
    fields = ("image",)
    extra = 1


@admin.register(Event)
class EventAdmin(NestedModelAdmin):
    inlines = [ImageTabularInline]  # see stories app
    search_fields = ["event_name", "content"]
    list_display = ["event_name", "start_date", "end_date"]
    list_filter = ["start_date", "end_date"]
