import pytest
from django.urls import reverse, resolve
from django.test import Client


class TestViews():
    """
    Views tests for the index and profiles object pages
    """
    @pytest.mark.usefixtures("profile_fixture")
    @pytest.mark.django_db
    def test_profile_index_view(self):
        # The view profiles_index needs to check this path and the right status code
        # to show this view
        client = Client()
        path = reverse('profiles_index')
        response = client.get(path)
        assert path == "/profiles/"
        assert response.status_code == 200
        assert resolve(path).view_name == "profiles_index"

    @pytest.mark.usefixtures("profile_fixture")
    @pytest.mark.django_db
    def test_profile_object_view(self):
        # The view profile needs to check this path and the right status code to show this view
        client = Client()
        path = reverse('profile', args=["Test"])
        response = client.get(path)
        assert path == "/profiles/Test/"
        assert response.status_code == 200
        assert resolve(path).view_name == "profile"
