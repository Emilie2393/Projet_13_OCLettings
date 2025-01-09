import pytest


class TestModels():
    """
    Test classe for the profile model of profiles app
    """
    @pytest.mark.usefixtures("profile_fixture")
    @pytest.mark.django_db
    def test_profile_model(self, profile_fixture):
        # profile_fixture needs to be check with the correct simulated value
        expected_value = "Test"
        assert str(profile_fixture) == expected_value
