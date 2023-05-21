from rest_framework.serializers import ModelSerializer

from .models import Cinemas, Movies, Showtimes


class CinemasSerializers(ModelSerializer):
    class Meta:
        model = Cinemas
        fields = ['title', 'tickets_phone', 'city', 'street', 'house', 'start_time', 'end_time']


class MoviesSerializers(ModelSerializer):
    class Meta:
        model = Movies
        fields = ['title', 'description', 'filmmaker', 'genre', 'age_limit', 'date_start', 'date_end']


class ShowtimesSerializers(ModelSerializer):
    class Meta:
        model = Showtimes
        fields = ['start_session', 'end_session', 'cinema', 'movie']
