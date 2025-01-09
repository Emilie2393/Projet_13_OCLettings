from django.test import Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed


class TestsIndex():
    """
    Tests for the index part of the website OCLettings
    """
    def test_index_url(self):
        # OCLettings index needs to be access with the following path
        path = reverse('index')
        assert path == "/"
        assert resolve(path).view_name == "index"

    def test_index_view(self):
        # The OCLettings index needs to check this path and the right status code to show this view
        client = Client()
        response = client.get(reverse("index"))
        content = "Welcome to Holiday Homes"
        assert content in response.content.decode()
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")
