from django.contrib import admin

from .models import Cinemas, MovieFormat,  Movies, Showtimes


admin.site.register(Cinemas)
admin.site.register(MovieFormat)
admin.site.register(Movies)
admin.site.register(Showtimes)
