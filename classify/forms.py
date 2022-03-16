from django.forms import ModelForm
from .models import Images


class SetInformationForm(ModelForm):  # Get image for classify
    class Meta:
        model = Images
        fields = ['image']
