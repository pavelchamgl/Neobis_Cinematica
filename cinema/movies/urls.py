from django.urls import path, include
from rest_framework import routers

from .endpoints import CinemasViewSet, MoviesViewSet, ShowtimesViewSet


router = routers.SimpleRouter()
router.register("cinema_viewset", CinemasViewSet)
router.register("movies_viewset", MoviesViewSet, basename="movies")
router.register("showtime_viewset", ShowtimesViewSet, basename="showtimes")


urlpatterns = [
    path("/", include(router.urls)),
]
