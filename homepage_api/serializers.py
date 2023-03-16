from rest_framework import serializers
from homepage_api.models import HomePageInfo

class HomeSerializer(serializers.ModelSerializer):
    class Meta : 
        model = HomePageInfo
        fields = "__all__"