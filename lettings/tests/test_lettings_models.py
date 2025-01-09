import pytest


class TestModels():
    """
    Test classe for the address model of lettings app
    """
    @pytest.mark.usefixtures("address_fixture")
    @pytest.mark.django_db
    def test_address_model(self, address_fixture):
        # address_fixture needs to be check with the correct simulated value
        expected_value = "5 rue du Test"
        assert str(address_fixture) == expected_value
