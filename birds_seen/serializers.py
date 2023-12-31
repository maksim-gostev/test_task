from rest_framework import serializers

from birds.models import Birds
from birds_seen.models import BirdsSeen

class BirdsSawSerializer(serializers.ModelSerializer):

    class Meta:
        model = Birds
        exclude = ['id', 'feather_color']


class Birds_seenSerializer(serializers.ModelSerializer):
    birds = BirdsSawSerializer()
    image_bird = serializers.ReadOnlyField(source='bird.picture')


    class Meta:
        model = BirdsSeen
        fields = '__all__'

