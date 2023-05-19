from django.urls import include, re_path


urlpatterns = [
    re_path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.jwt')),
]
