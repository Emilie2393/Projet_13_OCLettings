import pytest
from django.urls import reverse, resolve
from lettings.models import Address, Letting
 
def test_lettings_index_url():
    path = reverse('lettings_index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"


@pytest.mark.django_db
def test_letting_object_url():
    address = Address.objects.create(number=5, street="rue du Test", city="Rennes", state="FR", zip_code=35000, country_iso_code="FR")
    print(address)
    Letting.objects.create(title="test", address=1)
    path = reverse('letting', kwargs={'pk':1})
    
    assert path == "/1"
    assert resolve(path).view_name == "letting"


