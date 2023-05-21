from django.db import models


class Cinemas(models.Model):
    title = models.CharField(max_length=30)
    tickets_phone = models.IntegerField()
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    house = models.PositiveIntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.title} - {self.city}"

    class Meta:
        verbose_name = "Кинотеатор"
        verbose_name_plural = "Кинотеатры"


class Movies(models.Model):
    genre_choice = (
        ('1', 'action'),
        ('2', 'comedy'),
        ('3', 'melodrama'),
        ('4', 'drama'),
        ('5', 'horror'),
        ('6', 'fantasy'),
        ('7', 'cartoon'),
    )
    age_limit_choice = (
        ('1', '6+'),
        ('2', '12+'),
        ('3', '16+'),
        ('4', '18+'),
        ('5', '-'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    filmmaker = models.CharField(max_length=60)
    genre = models.CharField(max_length=10, choices=genre_choice)
    age_limit = models.CharField(max_length=4, choices=age_limit_choice, default='5')
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f"{self.id}: {self.title} - {self.genre} - {self.age_limit}"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Showtimes(models.Model):
    start_session = models.TimeField()
    end_session = models.TimeField()
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.cinema} - {self.movie} | {self.start_session} - {self.end_session}"

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"
