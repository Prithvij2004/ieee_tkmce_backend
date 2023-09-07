from django.contrib import admin

from .models import Team, TeamMember


@admin.register(TeamMember)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ["name", "position"]
    list_display = ["name", "position", "rank"]


admin.site.register(Team)
