import pytest
from lettings.models import Address, Letting


@pytest.fixture
def address_fixture():
    address = Address.objects.create(number=5,
                                     street="rue du Test",
                                     city="Rennes",
                                     state="FR",
                                     zip_code=35000,
                                     country_iso_code="FR")

    return address


@pytest.fixture
def letting_fixture(address_fixture):
    letting = Letting.objects.create(title="Test",
                                     address=address_fixture)

    return letting
