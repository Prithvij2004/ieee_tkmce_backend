from django.urls import path

from .views import message_as_view

app_name = "message"
urlpatterns = [
    path("", message_as_view, name="message"),
]
