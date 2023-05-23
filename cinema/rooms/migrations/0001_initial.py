# Generated by Django 4.1.7 on 2023-05-23 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("movies", "0002_alter_cinemas_options_alter_movies_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                (
                    "room_type",
                    models.CharField(
                        choices=[
                            ("1", "Small"),
                            ("2", "Big"),
                            ("3", "IMAX"),
                            ("4", "3D"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "cinemas",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.cinemas"
                    ),
                ),
                (
                    "showtimes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.showtimes",
                    ),
                ),
            ],
            options={
                "verbose_name": "Зал",
                "verbose_name_plural": "Залы",
            },
        ),
        migrations.CreateModel(
            name="Seat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seat", models.PositiveIntegerField()),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rooms.room"
                    ),
                ),
            ],
            options={
                "verbose_name": "Место",
                "verbose_name_plural": "Места",
            },
        ),
    ]