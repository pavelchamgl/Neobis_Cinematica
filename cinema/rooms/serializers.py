from rest_framework.serializers import ModelSerializer

from .models import Room, Seat


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'showtimes', 'room_type', 'cinemas']


class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = ['room', 'seat']
