from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from ieee_tkmce_backend.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
# urlpatterns = router.urls
urlpatterns = [
    path("team/", include("ieee_tkmce_backend.team.urls")),
    path("stats/", include("ieee_tkmce_backend.stats.urls")),
    path("stories/", include("ieee_tkmce_backend.stories.urls")),
    path("updates/", include("ieee_tkmce_backend.updates.urls")),
    path("awards/", include("ieee_tkmce_backend.awards.urls")),
    path("contact/", include("ieee_tkmce_backend.contact.urls")),
    path("message/", include("ieee_tkmce_backend.message.urls")),
    path("society/", include("ieee_tkmce_backend.society.urls")),
    path("home/", include("ieee_tkmce_backend.home.urls")),
]
