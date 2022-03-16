from django.shortcuts import render
from .forms import SetInformationForm
from django.http.response import HttpResponse


def index(request):  # first page of classify app

    if request.method == 'POST':
        form = SetInformationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Submitted successfully!')

        return HttpResponse(f"{form.errors}")
    if request.method == "GET":
        form = SetInformationForm()
        return render(request, "classify/classify.html", {'form': form})
