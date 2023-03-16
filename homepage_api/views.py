from django.shortcuts import render
from rest_framework.generics import ListAPIView
from homepage_api.models import HomePageInfo
from homepage_api.serializers import HomeSerializer

# dziedziczenie po ListAPIView
class GetHomePageInfoView(ListAPIView):
    serializer_class = HomeSerializer
    queryset = HomePageInfo.objects.all()
