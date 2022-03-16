from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path('login/', view=obtain_auth_token),
]
