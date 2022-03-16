from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .forms import SignUpForm
from django.http.response import HttpResponse


def index(request):
    # first page of users' model for select between signup or login

    return render(request, "users/index.html")


def signup(request):
    # signup users

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!')

        return HttpResponse(f"{form.errors}")
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'users/signUp.html', {'form': form})


class LoginAPIView(GenericAPIView):
    # login users

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={'message': f"Welcome to our website, {request.user.username}!"})


class LogoutAPIView(GenericAPIView):
    # logout users

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f"{request.user.username}, you have successfully logged out!"})
