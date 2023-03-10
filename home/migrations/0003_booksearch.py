# Generated by Django 4.1.5 on 2023-01-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_bookpost_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="bookSearch",
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
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("publisher", models.CharField(max_length=100)),
                ("pub_date", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
    ]
