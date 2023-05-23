from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractBaseUser


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class ClubCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.email} {self.balance} - {self.discount}"

    class Meta:
        verbose_name = "ClubCard"
        verbose_name_plural = "ClubCards"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.email}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
