import pytest
from django.urls import reverse
from birds_seen.serializers import BirdsSeenSerializer
from tests.factories import BirdsSeenFactory

@pytest.mark.django_db
def test_list_birds_seen(client):
    birds_seen = BirdsSeenFactory.create_batch(10)

    expected_response = BirdsSeenSerializer(birds_seen, many=True).data


    response = client.get(reverse('birds_seen:saw_list'))

    assert response.status_code == 200
    assert response.json() == expected_response