from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model


user_model = get_user_model()

class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    def create(self, validated_data):
        print (validated_data, flush=True)
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        # terms = validated_data['terms']

        user = user_model.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name )

        return user

    class Meta:
        model = user_model
        fields = ("id", "username", "password", "first_name", "last_name", "email")