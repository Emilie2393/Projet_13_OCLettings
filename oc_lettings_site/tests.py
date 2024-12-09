from django.test import Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed
 
def test_index_url():
    path = reverse('index')
    assert path == "/"
    assert resolve(path).view_name == "index"

def test_index_view():
    client = Client()
    response = client.get(reverse("index"))
    content = "Welcome to Holiday Homes"
    assert content in response.content.decode()
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


