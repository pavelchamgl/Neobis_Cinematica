from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError

from .models import Booking, Order, Ticket


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'seat', 'showtime']

    def validate(self, data):
        seat = data.get('seats')
        showtime = data.get('showtime')
        if Booking.objects.filter(seat=seat, showtime=showtime).exists():
            raise ValidationError('Это место уже забронированно!')
        return data


class OrderSerializer(ModelSerializer):
    total_price = SerializerMethodField('get_total_price')

    def get_total_price(self, obj):
        tickets = Ticket.objects.filter(order_id=obj.id)
        total_price = 0
        for ticket in tickets:
            total_price += ticket.price
        return total_price

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price']


class TicketSerializer(ModelSerializer):

    def validate(self, data):
        seat = data.get('seats_id')
        showtime = data.get('showtime')
        if Booking.objects.filter(seat=seat, showtime=showtime).exists():
            raise ValidationError('Это место уже забронированно!')
        return data

    class Meta:
        model = Ticket
        fields = ['id', 'ticket_type', 'price', 'user', 'seats_id', 'order_id', 'showtime']
