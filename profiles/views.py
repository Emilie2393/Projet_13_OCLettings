from django.shortcuts import render
from .models import Profile
from sentry_sdk import capture_message


# Index page for profiles part
def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Profile page for each username
def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
    except Exception as e:
        capture_message("This id doesn't exist", e)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
