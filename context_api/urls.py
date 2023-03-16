from django.contrib import admin
from django.urls import path, include

from context_api.views import GetNavbarOptionsView

urlpatterns = [
    path('navbar-options/', GetNavbarOptionsView.as_view()),
]

# pip install django-cors-headers w terminalu, zeby ogarnac CORS error w konsoli na froncie