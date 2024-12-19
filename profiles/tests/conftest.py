import pytest
from profiles.models import Profile
from django.contrib.auth.models import User

@pytest.fixture
def profile_fixture():
    user = User.objects.create_user(username="Test",
                                    email="test@test.fr",
                                    password="test")
    profile = Profile.objects.create(user=user,
                                     favorite_city="Rennes")
    
    return profile


