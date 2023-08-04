from django.http import JsonResponse
from django.views import View
from rest_framework import generics

from birds.models import Birds
from birds.serializers import BirdsSerializer
from constants import CUSTOM_LISTS_TEMPLATE


class BirdListView(View):
    def get(self, request):
        birds = Birds.objects.all()

        CUSTOM_LISTS_TEMPLATE["customcards"]["cardsdata"]=[]
        for bird in birds:
            if hasattr(bird, "image"):
                CUSTOM_LISTS_TEMPLATE["customcards"]["cardsdata"].append({
                    "id": bird.id,
                    "name": bird.name,
                    'image': bird.image,
                })
            CUSTOM_LISTS_TEMPLATE["customcards"]["cardsdata"].append({
                "id": bird.id,
                "name": bird.name,
            })
        return JsonResponse(CUSTOM_LISTS_TEMPLATE, safe=False)

class BirdCreateView(generics.CreateAPIView):
    serializer_class = BirdsSerializer


class BirdDetailView(generics.RetrieveAPIView):
    queryset = Birds.objects.all()
    serializer_class = BirdsSerializer

