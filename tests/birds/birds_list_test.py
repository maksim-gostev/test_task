import pytest
from django.urls import reverse
from birds.serializers import BirdsSerializer
from constants import CUSTOM_LISTS_TEMPLATE
from tests.factories import BirdsFactory



@pytest.mark.django_db
def test_list_birds(client):
    birds = BirdsFactory.create_batch(3)

    CUSTOM_LISTS_TEMPLATE["customcards"]["cardsdata"] = []

    for bird in birds:
        CUSTOM_LISTS_TEMPLATE["customcards"]["cardsdata"].append(BirdsSerializer(bird).data)

    response = client.get(reverse('birds:bird_list'))


    assert response.status_code == 200
    assert response.json() == CUSTOM_LISTS_TEMPLATE