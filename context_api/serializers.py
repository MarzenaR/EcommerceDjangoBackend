from rest_framework import serializers
from context_api.models import NavbarOptions

class NavbarSerializer(serializers.ModelSerializer):
    class Meta : 
        model = NavbarOptions
        fields = "__all__"