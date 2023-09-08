# Generated by Django 4.2.4 on 2023-09-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Award",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("designation", models.CharField(max_length=50)),
                ("content", models.CharField(max_length=300)),
                ("priority", models.IntegerField(choices=[(1, "HIGH"), (0, "LOW")], default=0)),
                ("image", models.ImageField(upload_to="images/awards/")),
                ("slug", models.SlugField(blank=True, editable=False, max_length=150, unique=True)),
                ("pub_date", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "ordering": ["-priority", "-pub_date"],
            },
        ),
    ]