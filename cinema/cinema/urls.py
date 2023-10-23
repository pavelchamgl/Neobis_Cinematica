from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('users.urls')),
    path("movies/", include('movies.urls')),
    path("room/", include('rooms.urls')),
    path("order/", include('orders.urls')),
]
