from dataclasses import field
from .models import *
from rest_framework import serializers

class KrosovkaAPI(serializers.ModelSerializer):
    class Meta:
        model = Krosovka
        fields = '__all__'

class CarsAPI(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'