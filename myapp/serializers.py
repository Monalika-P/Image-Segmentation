
from .models import *
from rest_framework import serializers


class SegmentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Segmentation

        fields = '__all__'

