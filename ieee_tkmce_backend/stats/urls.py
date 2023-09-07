from django.urls import path

from .views import stats_all_as_view, stats_each_as_view

app_name = "stats"
urlpatterns = [
    path("", stats_all_as_view, name="all"),
    path("<slug:slug>/", stats_each_as_view, name="stats_each")
    # slug is matched with the slug in Retrieve API View
]
