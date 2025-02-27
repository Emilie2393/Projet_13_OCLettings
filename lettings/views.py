from django.shortcuts import render
from .models import Letting
from sentry_sdk import capture_message


# Index page for the lettings part
def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Letting specific id section
def letting(request, letting_id):
    try:
        letting = Letting.objects.get(id=letting_id)
    except Exception as e:
        capture_message("This id doesn't exist", e)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/lettings.html', context)
