from django.urls import path

from .views import team_as_view

app_name = "team"
urlpatterns = [
    path("", team_as_view, name="team"),
]
