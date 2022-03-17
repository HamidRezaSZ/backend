from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.contrib import messages

from .forms import SignUpForm


def index(request):  # first page of users' app for select between signup or login
    if request.method == "GET":
        form_sign = SignUpForm()  # signup form
        form_log = AuthenticationForm()  # login form
        return render(request, 'users/index.html', {'formSign': form_sign, 'formLog': form_log})

    if request.method == 'POST':
        form_sign = SignUpForm(request.POST)  # signup user
        if form_sign.is_valid():
            form_sign.save()
            messages.success(request, "User created successfully!")
            return HttpResponseRedirect(reverse("index"))

        form_log = AuthenticationForm(request=request, data=request.POST)  # login users
        if form_log.is_valid():
            username = form_log.cleaned_data.get('username')
            password = form_log.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                Token.objects.get_or_create(user=user)
                login(request, user)
                return HttpResponseRedirect(reverse("classify:index"))

            else:
                messages.error(request, "Invalid username or password!")
                return HttpResponseRedirect(reverse("index"))

        messages.error(request, "Error!")
        return HttpResponseRedirect(reverse("index"))


def logout_request(request):  # logout users

    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'You successfully logged out!')
        return HttpResponseRedirect(reverse("index"))

    if request.method == "GET":
        messages.error(request, 'Only POST method allowed!')
        return HttpResponseRedirect(reverse("index"))
