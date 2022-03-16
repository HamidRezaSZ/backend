from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login

from .forms import SignUpForm


def index(request):  # first page of users' app for select between signup or login
    return render(request, "users/index.html")


def signup(request):  # signup users
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!')

        return HttpResponse(f"{form.errors}")
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'users/signUp.html', {'form': form})


def login_request(request):  # login users
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("classify:index"))

            else:
                return HttpResponse("Invalid username or password.")

        else:
            return HttpResponse("Invalid username or password.")

    if request.method == "GET":
        form = AuthenticationForm()
        return render(request=request,
                      template_name="users/logIn.html",
                      context={"form": form})


def logout_request(request):  # logout users
    logout(request)
    return HttpResponse("Logged out successfully!")
