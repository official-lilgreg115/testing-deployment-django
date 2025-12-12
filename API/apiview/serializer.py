from rest_framework import serializers
from .models import Data,SmallData,SmallestData

class SmallestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallestData
        fields = '__all__'

class SmallDataSerializer(serializers.ModelSerializer):
    inside = SmallestDataSerializer()
    class Meta:
        model = SmallData
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    insert = SmallDataSerializer()
    inside = SmallestDataSerializer()
    class Meta:
        model = Data
        fields = ['name','age','insert','inside']