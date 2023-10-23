from rest_framework.serializers import ModelSerializer

from .models import User, ClubCard, Feedback


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'birthday', 'phone']


class ClubCardSerializer(ModelSerializer):
    class Meta:
        model = ClubCard
        fields = ['id', 'user', 'balance', 'discount']


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'text']
