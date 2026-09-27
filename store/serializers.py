from rest_framework import serializers
from .models import Sneaker

class SneakerSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = Sneaker
        fields = ['id', 'title', 'brand', 'sizes', 'description', 'image', 'gallery', 'price', 'discount', 'feature', 'rating']