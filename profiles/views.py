from django.shortcuts import render
from .models import Profile
from sentry_sdk import capture_message
from django.shortcuts import get_object_or_404
from django.http import Http404


# Index page for profiles part
def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Profile page for each username
def profile(request, username):
    try:
        profile = get_object_or_404(Profile, user__username=username)
    except Exception as e:
        capture_message("This profile's id doesn't exist", e)
        raise Http404("This profile's id doesn't exist")
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
