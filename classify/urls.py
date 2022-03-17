from django.urls import path
from . import views

app_name = "classify"
urlpatterns = [
    path('', views.index, name="index"),
]
