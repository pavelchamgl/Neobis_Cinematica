from django.urls import path, include
from rest_framework import routers

from .endpoints import RoomViewSet, SeatViewSet


router = routers.SimpleRouter()
router.register("room_viewset", RoomViewSet)
router.register("seat_viewset", SeatViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
