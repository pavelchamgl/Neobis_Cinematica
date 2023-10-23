from django.contrib import admin

from .models import RoomType, Room, Seat


admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Seat)
