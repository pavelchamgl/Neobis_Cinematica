from django.db import models


class RoomType(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.name} - {self.price}"

    class Meta:
        verbose_name = "Тип зала"
        verbose_name_plural = "Типы залов"


class Room(models.Model):
    name = models.CharField(max_length=20)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name} - {self.room_type}"

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
