from rest_framework import serializers
from homepage_api.models import CompanyInfo

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta : 
        model = CompanyInfo
        fields = "__all__"