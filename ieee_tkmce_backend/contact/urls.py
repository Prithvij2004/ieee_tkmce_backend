from django.urls import path

from .views import contact_as_view

app_name = "contact"
urlpatterns = [
    path("", contact_as_view, name="contact"),
]
