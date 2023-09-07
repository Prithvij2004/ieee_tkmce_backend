from django.urls import path

from .views import award_all_as_view, award_each_as_view

app_name = "awards"
urlpatterns = [
    path("", award_all_as_view, name="get_all_awards"),
    path("<slug:slug>/", award_each_as_view, name="award_each"),
]
