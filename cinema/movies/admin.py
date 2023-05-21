from django.contrib import admin

from .models import Cinemas, Movies, Showtimes


admin.site.register(Cinemas)
admin.site.register(Movies)
admin.site.register(Showtimes)
