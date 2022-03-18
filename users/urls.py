from django.urls import path
from .views import Logout, Register, Login

app_name = "users"
urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('register/', Register.as_view(), name="register"),
]
