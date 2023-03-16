from django.shortcuts import render
from rest_framework.generics import ListAPIView
from homepage_api.models import HomePageInfo
from contact_us_api.serializers import CompanyInfoSerializer

# dziedziczenie po ListAPIView
class GetCompanyInfoView(ListAPIView):
    serializer_class = CompanyInfoSerializer
    queryset = HomePageInfo.objects.all()

