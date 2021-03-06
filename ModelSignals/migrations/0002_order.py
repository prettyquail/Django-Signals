# Generated by Django 3.1 on 2021-06-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ModelSignals", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("total", models.PositiveIntegerField(blank=True)),
                ("total_price", models.PositiveIntegerField(blank=True)),
                ("active", models.BooleanField(default=True)),
                ("cars", models.ManyToManyField(to="ModelSignals.Car")),
            ],
        ),
    ]
