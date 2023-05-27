from django.contrib import admin

from .models import Booking, Order, TicketType, Ticket
admin.site.register(Booking)
admin.site.register(Order)
admin.site.register(TicketType)
admin.site.register(Ticket)
