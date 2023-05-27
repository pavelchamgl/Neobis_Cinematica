from django.urls import path, include
from rest_framework import routers

from .endpoints import BookingViewSet, OrderViewSet, TicketViewSet


router = routers.SimpleRouter()
router.register("booking_viewset", BookingViewSet)
router.register("order_viewset", OrderViewSet)
router.register("ticket_viewset", TicketViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
