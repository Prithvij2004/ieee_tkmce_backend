from django.urls import path
from .views import god_as_view
app_name="home"
urlpatterns=[
    path('',god_as_view,name="home")
]
