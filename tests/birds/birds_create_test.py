import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_birds(client):
    expected_response = {
        'id': 1,
        'name': 'test',
        'feather_color':'blue',
        'picture': None
    }

    data = {
        'name': 'test',
        'feather_color':'blue'
    }


    response = client.post(reverse('birds:bird_create'), data=data)


    assert response.status_code == 201
    assert response.json() == expected_response