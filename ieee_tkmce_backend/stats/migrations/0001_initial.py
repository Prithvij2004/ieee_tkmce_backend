# Generated by Django 4.2.4 on 2023-09-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stats",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, unique=True)),
                ("value", models.IntegerField()),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "Statistics",
                "verbose_name_plural": "Statistics",
            },
        ),
    ]
