from rest_framework import serializers

from birds.models import Birds


class BirdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Birds
        fields = '__all__'
