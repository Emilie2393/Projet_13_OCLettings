from django.contrib import admin
from django.urls import path, include
from .views import custom_404
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls, name='admin'),
]

handler404 = custom_404
