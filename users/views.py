from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


def index(request):  # first page of users' app for select between signup or login
    return render(request, 'users/index.html')


class Register(CreateAPIView):  # signup users
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            messages.success(request, "User created successfully!")
            return HttpResponseRedirect(reverse("index"))
        messages.error(request, f"{user_serializer.errors}")
        return HttpResponseRedirect(reverse("index"))

    def get(self, request):
        return HttpResponseRedirect(reverse("index"))


class Logout(APIView):  # logout users

    def post(self, request):
        messages.success(request, 'You successfully logged out!')
        return HttpResponseRedirect(reverse("index"))

    def get(self, request):
        return HttpResponseRedirect(reverse("index"))


class Login(ObtainAuthToken):  # login users

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)  # create token
            return HttpResponseRedirect(reverse("classify:index"))
        messages.error(request, f"{serializer.errors}")
        return HttpResponseRedirect(reverse("index"))

    def get(self, request):
        return HttpResponseRedirect(reverse("index"))
