import pytest
from conftest import address_fixture

@pytest.mark.django_db  
def test_address_model(address_fixture):
    expected_value = "5 rue du Test"
    assert str(address_fixture) == expected_value