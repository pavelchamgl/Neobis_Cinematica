from django.db.models import Subquery
from rest_framework.generics import ListAPIView
from datetime import datetime

from .models import Cinemas, Movies, Showtimes
from .serializers import CinemasSerializers, MoviesSerializers, ShowtimesSerializers


class CinemasLislAPIView(ListAPIView):
    serializer_class = CinemasSerializers
    queryset = Cinemas.objects.all()


class MoviesLislAPIView(ListAPIView):
    serializer_class = MoviesSerializers

    def get_queryset(self):
        current_date = datetime.today().date()
        movies = Movies.objects.filter(date_start__gte=current_date, date_end__lte=current_date)
        return movies


class ShowtimesLislAPIView(ListAPIView):
    serializer_class = ShowtimesSerializers

    def get_queryset(self):
        current_date = datetime.today()
        movies = Movies.objects.filter(date_end__gte=current_date.date())
        showtimes = Showtimes.objects.filter(movie__in=Subquery(movies.values("id")))
        current_showtimes = showtimes.filter(start_session__gte=current_date.time())
        return current_showtimes

