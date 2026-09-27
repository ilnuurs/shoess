from rest_framework import serializers
from .models import Sneaker

class SneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneaker
        fields = ['id', 'title', 'brand', 'sizes', 'color', 'description', 'image', 'price', 'discount', 'feature', 'rating']