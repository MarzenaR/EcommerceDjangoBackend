from django.shortcuts import render
from rest_framework.generics import ListAPIView
from context_api.models import NavbarOptions
from context_api.serializers import NavbarSerializer

class GetNavbarOptionsView(ListAPIView):
    serializer_class = NavbarSerializer
    queryset = NavbarOptions.objects.all()