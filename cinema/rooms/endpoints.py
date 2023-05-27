from rest_framework.viewsets import ModelViewSet

from .serializers import RoomTypeSerializer, RoomSerializer, SeatSerializer
from .models import Room, Seat, RoomType
from users.permissions import IsAdminOrReadOnly


class RoomTypeViewSet(ModelViewSet):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class SeatViewSet(ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()
    permission_classes = [IsAdminOrReadOnly]
