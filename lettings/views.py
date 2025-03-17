from django.shortcuts import render
from .models import Letting
from sentry_sdk import capture_message
from django.shortcuts import get_object_or_404


# Index page for the lettings part
def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Letting specific id section
def letting(request, letting_id):
    try:
        letting = get_object_or_404(Letting, id=letting_id)
    except Exception as e:
        capture_message("This letting's id doesn't exist", e)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/lettings.html', context)
