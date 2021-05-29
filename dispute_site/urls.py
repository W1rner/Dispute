from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from dispute_site.views import about_page

urlpatterns = [
    path('', about_page),
    path('popular/', popular_page)
    ]
