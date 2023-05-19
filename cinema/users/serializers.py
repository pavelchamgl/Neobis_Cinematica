from rest_framework.serializers import ModelSerializer

from .models import User


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'birthday', 'phone']
