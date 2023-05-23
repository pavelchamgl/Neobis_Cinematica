from django.contrib import admin

from .models import User, ClubCard, Feedback


admin.site.register(User)
admin.site.register(ClubCard)
admin.site.register(Feedback)
