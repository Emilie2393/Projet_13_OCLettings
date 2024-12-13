import pytest
from django.urls import reverse, resolve
from django.test import Client
from lettings.models import Address, Letting
 
def test_lettings_index_url():
    path = reverse('lettings_index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"


@pytest.mark.django_db
def test_letting_object_url():
    address = Address.objects.create(number=5, street="rue du Test", city="Rennes", state="FR", zip_code=35000, country_iso_code="FR")
    Letting.objects.create(title="test", address=address)
    path = reverse('letting', args=[1])
    
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "letting"


