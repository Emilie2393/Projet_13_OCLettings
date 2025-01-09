import pytest
from django.urls import reverse, resolve
from django.test import Client


class TestViews():
    """
    Views tests for the index and lettings object pages
    """
    @pytest.mark.usefixtures("letting_fixture")
    @pytest.mark.django_db
    def test_letting_index_view(self):
        # The view lettings_index needs to check this path and the right status code to
        # show this view
        client = Client()
        path = reverse('lettings_index')
        response = client.get(path)
        assert path == "/lettings/"
        assert response.status_code == 200
        assert resolve(path).view_name == "lettings_index"

    @pytest.mark.usefixtures("letting_fixture")
    @pytest.mark.django_db
    def test_letting_object_view(self, letting_fixture):
        client = Client()
        path = reverse('letting', args=[1])
        response = client.get(path)
        assert path == "/lettings/1/"
        assert response.status_code == 200
        assert resolve(path).view_name == "letting"
