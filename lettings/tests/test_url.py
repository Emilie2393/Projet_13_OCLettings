from django.urls import reverse, resolve

 
def test_lettings_index_url():
    path = reverse('lettings_index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"

def test_lettings_letting_url():
    path = reverse('letting', args=[1])
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "letting"




