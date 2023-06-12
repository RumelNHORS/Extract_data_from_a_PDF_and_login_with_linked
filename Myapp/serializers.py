from rest_framework import serializers
from . models import ScrapedDataModel, EduDataModel

class ScrapedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedDataModel
        fields = "__all__"

class EduSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduDataModel
        fields = "__all__"