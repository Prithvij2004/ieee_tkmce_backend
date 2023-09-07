from django.urls import path

from .views import society_as_view, society_each_as_view

app_name = "society"
urlpatterns = [
    path("", society_as_view, name="society"),
    path("<slug:slug>", society_each_as_view, name="each_society"),
]
