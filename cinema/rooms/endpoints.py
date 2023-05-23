from rest_framework.viewsets import ModelViewSet

from .serializers import RoomSerializer, SeatSerializer
from .models import Room, Seat
from users.permissions import IsAdminOrReadOnly


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class SeatViewSet(ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()
    permission_classes = [IsAdminOrReadOnly]
