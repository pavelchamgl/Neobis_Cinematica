from django.db import models

from movies.models import Showtimes, Cinemas


class Room(models.Model):
    room_type_choice = (
        ('1', 'Small'),
        ('2', 'Big'),
        ('3', 'IMAX'),
        ('4', '3D'),
    )
    name = models.CharField(max_length=20)
    showtimes = models.ForeignKey(Showtimes, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=10, choices=room_type_choice)
    cinemas = models.ForeignKey(Cinemas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name} - {self.room_type} - {self.cinemas}"

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id}: {self.room} - {self.seat}"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
