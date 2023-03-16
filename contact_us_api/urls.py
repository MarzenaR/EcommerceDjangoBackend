from django.contrib import admin
from django.urls import path, include

from contact_us_api.views import GetCompanyInfoView

urlpatterns = [
    path('company-info/', GetCompanyInfoView.as_view()),
]