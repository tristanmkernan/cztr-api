import pytest

from django.urls import reverse
from rest_framework import status


def test_tests():
    assert True, "Tests work!"


@pytest.mark.django_db
@pytest.mark.usefixtures('seed_entries')
def test_query(client):
    response = client.get(reverse('query'), {'q': 'aardvark'})

    assert response.status_code == status.HTTP_200_OK



@pytest.mark.django_db
def test_transcribe(client):
    response = client.get(reverse('transcribe'), {'content': 'aardvark'})

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
@pytest.mark.usefixtures('seed_sentences')
def test_random(client):
    response = client.get(reverse('random'))

    assert response.status_code == status.HTTP_200_OK
