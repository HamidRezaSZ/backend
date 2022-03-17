from django.shortcuts import render
from .forms import SetInformationForm
from PIL import Image
import numpy
from keras.models import load_model
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.urls import reverse

model = load_model('classify/CIFAR10.h5')  # use ready file for increase performance

classes = {  # dataset labels
    0: 'aeroplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck'
}


def tensor_flow(file_path):  # tensorFlow function get image, predict label of that and return
    image = Image.open(file_path)
    image = image.resize((32, 32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    predict_X = model.predict(image)
    classes_X = numpy.argmax(predict_X, axis=1)
    result = classes[classes_X[0]]
    return result


def index(request):  # first page of classify app
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetInformationForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                image = form.cleaned_data.get("image")
                title = tensor_flow(image)
                img_obj = form.instance
                return render(request, "classify/classify.html", {'title': title, 'image': img_obj})

            messages.error(request, f"{form.errors}")
            return HttpResponseRedirect(reverse("classify:index"))

        if request.method == "GET":
            form = SetInformationForm()
            return render(request, "classify/classify.html", {'form': form})

    messages.error(request, 'You are not login!')
    return HttpResponseRedirect(reverse("index"))
