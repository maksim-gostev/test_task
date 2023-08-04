from rest_framework import generics

from birds.models import Birds
from birds.serializers import BirdsSerializer


class BirdListView(generics.ListAPIView):
    queryset = Birds.objects.all()
    serializer_class = BirdsSerializer


class BirdCreateView(generics.CreateAPIView):
    serializer_class = BirdsSerializer


class BirdDetailView(generics.RetrieveAPIView):
    queryset = Birds.objects.all()
    serializer_class = BirdsSerializer

