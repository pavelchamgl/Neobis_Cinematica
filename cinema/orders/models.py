from django.db import models

from users.models import User, ClubCard
from movies.models import Showtimes
from rooms.models import Seat


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtimes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.seat} - {self.showtime}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Бронь"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}: {self.total_price}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class TicketType(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.price}"

    class Meta:
        verbose_name = "Тип билета"
        verbose_name_plural = "Типы билетов"


class Ticket(models.Model):
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtimes, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        price = (self.ticket_type.price + self.showtime.rooms.room_type.price + self.showtime.movie.movie_format.price)
        club_card = ClubCard.objects.filter(user=self.user).first()
        discount = club_card.discount
        if discount == 0:
            self.price = price
        else:
            price_with_discount = (price / 100 * discount)
            self.price = (price - price_with_discount)

        super().save(*args, **kwargs)
