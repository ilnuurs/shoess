
from rest_framework import generics
from .models import Sneaker
from .serializers import SneakerSerializer


class SneakerListView(generics.ListAPIView):
    queryset = Sneaker.objects.all()
    serializer_class = SneakerSerializer