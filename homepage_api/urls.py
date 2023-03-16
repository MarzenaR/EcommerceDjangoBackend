from django.contrib import admin
from django.urls import path, include

from homepage_api.views import GetHomePageInfoView

urlpatterns = [
    path('description/', GetHomePageInfoView.as_view()),
]