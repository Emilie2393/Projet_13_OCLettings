from django.urls import reverse, resolve

class TestUrl():
    """
    Urls tests for the index and lettings pages
    """
    def test_lettings_index_url(self):
        # lettings index needs to be access with the following path
        path = reverse('lettings_index')
        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings_index"

    def test_lettings_letting_url(self):
        # letting object needs to be access with the following path
        path = reverse('letting', args=[1])
        assert path == "/lettings/1/"
        assert resolve(path).view_name == "letting"




