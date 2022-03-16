from django.shortcuts import render
from .forms import SetInformationForm
from django.http.response import HttpResponse


def tensor_flow(image):
    pass


def index(request):  # first page of classify app

    if request.method == 'POST':
        form = SetInformationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            image = form.cleaned_data.get("url")
            tensor_flow(image)
            return HttpResponse('Submitted successfully!')

        return HttpResponse(f"{form.errors}")
    if request.method == "GET":
        form = SetInformationForm()
        return render(request, "classify/classify.html", {'form': form})
