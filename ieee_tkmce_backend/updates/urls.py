from django.urls import path

from .views import event_all_as_view, event_each_as_view

app_name = "updates"
urlpatterns = [
    path("", event_all_as_view, name="get_all"),
    path("<slug:slug>/", event_each_as_view, name="event_each"),
]
