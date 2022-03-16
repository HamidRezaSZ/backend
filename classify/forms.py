from django.forms import ModelForm
from .models import Images


class SetInformationForm(ModelForm):  # Get information for classify images
    class Meta:
        model = Images
        fields = ['url']
