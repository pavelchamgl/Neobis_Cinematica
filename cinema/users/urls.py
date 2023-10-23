from django.urls import include, re_path, path
from rest_framework import routers

from .endpoints import ClubCardViewSet, FeedbackViewSet


router = routers.SimpleRouter()
router.register("club_card_viewset", ClubCardViewSet, basename="club_card")
router.register("feedback_viewset", FeedbackViewSet, basename="feedback")


urlpatterns = [
    re_path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.jwt')),
    path("", include(router.urls)),
]
