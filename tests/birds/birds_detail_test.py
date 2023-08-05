import pytest
from django.urls import reverse
from tests.factories import BirdsFactory



@pytest.mark.django_db
def test_deteil_birds(client):
    bird = BirdsFactory.create()

    expected_response = {
        'id': bird.id,
        'name': bird.name,
        'feather_color': bird.feather_color,
        'picture': bird.picture
    }
    response = client.get(reverse('birds:bird_detail', kwargs={'pk': bird.id}))


    assert response.status_code == 200
    assert response.json() == expected_response