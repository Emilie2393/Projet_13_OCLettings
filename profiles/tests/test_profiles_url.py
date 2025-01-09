from django.urls import reverse, resolve


class TestUrl():
    """
    Urls tests for the index and profiles pages
    """
    def test_profiles_index_url(self):
        # profiles index needs to be access with the following path
        path = reverse('profiles_index')
        assert path == "/profiles/"
        assert resolve(path).view_name == "profiles_index"

    def test_profiles_profile_url(self):
        # profiles object needs to be access with the following path
        path = reverse('profile', args=[1])
        assert path == "/profiles/1/"
        assert resolve(path).view_name == "profile"
