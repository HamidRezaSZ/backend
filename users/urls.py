from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("logout/", views.logout_request, name="logout"),
]
