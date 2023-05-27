from django.urls import path, include
from rest_framework import routers

from .endpoints import RoomTypeViewSet, RoomViewSet, SeatViewSet


router = routers.SimpleRouter()
router.register("room_type_viewset", RoomTypeViewSet)
router.register("room_viewset", RoomViewSet)
router.register("seat_viewset", SeatViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
