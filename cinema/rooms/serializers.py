from rest_framework.serializers import ModelSerializer

from .models import RoomType, Room, Seat


class RoomTypeSerializer(ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'name', 'price']


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'room_type']


class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'room', 'seat']
