from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from django.db.models import Subquery

from .models import Cinemas, Movies, Showtimes, MovieFormat
from .serializers import CinemasSerializers, MovieFormatSerializers, MoviesSerializers, ShowtimesSerializers
from users.permissions import IsAdminOrReadOnly


class CinemasViewSet(ModelViewSet):
    serializer_class = CinemasSerializers
    queryset = Cinemas.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class MovieFormatViewSet(ModelViewSet):
    serializer_class = MovieFormatSerializers
    queryset = MovieFormat.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class MoviesViewSet(ModelViewSet):
    serializer_class = MoviesSerializers
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        current_date = datetime.today().date()
        movies = Movies.objects.filter(date_start__gte=current_date, date_end__lte=current_date)
        return movies


class ShowtimesViewSet(ModelViewSet):
    serializer_class = ShowtimesSerializers
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        current_date = datetime.today()
        movies = Movies.objects.filter(date_end__gte=current_date.date())
        showtimes = Showtimes.objects.filter(movie__in=Subquery(movies.values("id")))
        current_showtimes = showtimes.filter(start_session__gte=current_date.time())
        return current_showtimes

