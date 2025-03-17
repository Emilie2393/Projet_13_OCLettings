from django.shortcuts import render


# Index page for Orange County Lettings website
def index(request):
    return render(request, 'index.html')

