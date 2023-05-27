from rest_framework.serializers import ModelSerializer

from .models import Cinemas, Movies, Showtimes, MovieFormat


class CinemasSerializers(ModelSerializer):
    class Meta:
        model = Cinemas
        fields = ['id', 'title', 'tickets_phone', 'city', 'street', 'house', 'start_time', 'end_time']


class MovieFormatSerializers(ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = ['id', 'name', 'price']


class MoviesSerializers(ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'title', 'description', 'filmmaker', 'genre', 'age_limit', 'date_start', 'date_end']


class ShowtimesSerializers(ModelSerializer):
    class Meta:
        model = Showtimes
        fields = ['id', 'start_session', 'end_session', 'cinema', 'movie']
