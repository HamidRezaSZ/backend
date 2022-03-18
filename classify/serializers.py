from rest_framework import serializers
from .models import Images


class SetInformationSerializer(serializers.ModelSerializer):  # Image model serializers
    class Meta:
        model = Images
        fields = ['image']
