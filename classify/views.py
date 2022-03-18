from django.shortcuts import render
from .serializers import SetInformationSerializer
from PIL import Image
import numpy
from keras.models import load_model
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from rest_framework.generics import GenericAPIView

model = load_model('classify/CIFAR10.h5')  # use ready file for increase performance

classes = {  # dataset labels
    0: 'airplane',
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


class Index(GenericAPIView):  # first page of classify app
    serializer_class = SetInformationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            image = serializer.validated_data['image']
            title = tensor_flow(image)
            img_obj = serializer.instance
            return render(request, "classify/classify.html", {'title': title, 'image': img_obj})

        messages.error(request, f"{serializer.errors}")
        return HttpResponseRedirect(reverse("classify:index"))

    def get(self, request):
        return render(request, 'classify/classify.html')
