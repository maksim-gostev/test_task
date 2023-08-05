import pytest
from django.urls import reverse
from tests.factories import BirdsSeenFactory

@pytest.mark.django_db
def test_deteil_birds_seen(client):
    birds_seen = BirdsSeenFactory.create()

    expected_response = {
        'id': birds_seen.id,
        'updated': birds_seen.updated.isoformat(),
        'number_vision_acts': birds_seen.number_vision_acts,
        'birds' : birds_seen.birds
    }

    response = client.get(reverse('birds_seen:saw', kwargs={'pk': birds_seen.id}))

    assert response.status_code == 302
    assert response.url == reverse('birds_seen:saw_list')