from datetime import datetime

from django.db.models import QuerySet
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.shortcuts import redirect
from rest_framework import generics
from birds.models import Birds
from birds_seen.models import Birds_seen
from birds_seen.serializers import Birds_seenSerializer
import global_variable


@method_decorator(csrf_exempt, name='dispatch')
class SawView(DetailView):
    model = Birds


    def get(self, request, *args, **kwargs):
        bird: Birds = self.get_object()

        global_variable.BIRDS_SEEN = {}

        global_variable.BIRDS_SEEN = {
            'bird': bird,
            'updated': datetime.utcnow(),
        }

        response = redirect('birds_seen:saw_list')
        return response

    def post(self, request, *args, **kwargs):

        try:
            birds_seen: QuerySet = Birds_seen.objects.filter(birds=global_variable.BIRDS_SEEN['bird']).first()
        except Birds_seen.DoesNotExist:
            birds_seen = None

        if birds_seen is None:
            obj: Birds_seen = Birds_seen(birds=global_variable.BIRDS_SEEN.get('bird'), updated=global_variable.BIRDS_SEEN.get('updated'))
            obj.save()
        else:
            obj: Birds_seen = Birds_seen.objects.filter(birds=global_variable.BIRDS_SEEN.get('bird')).first()
            obj.updated = global_variable.BIRDS_SEEN.get('updated')
            obj.number_vision_acts = obj.number_vision_acts + 1
            obj.save()

        global_variable.BIRDS_SEEN = {}

        return JsonResponse(Birds_seenSerializer(obj).data)

class Birds_I_saw_View(generics.ListAPIView):
    model = Birds_seen
    queryset = Birds_seen.objects.all()
    serializer_class = Birds_seenSerializer

