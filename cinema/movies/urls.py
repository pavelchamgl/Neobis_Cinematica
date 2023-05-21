from django.urls import path

from .endpoints import CinemasLislAPIView, MoviesLislAPIView, ShowtimesLislAPIView

urlpatterns = [
    path("", MoviesLislAPIView.as_view(), name='movies'),
    path("cinemas/", CinemasLislAPIView.as_view(), name='cinemas'),
    path("showtimes/", ShowtimesLislAPIView.as_view(), name='showtimes'),
]
