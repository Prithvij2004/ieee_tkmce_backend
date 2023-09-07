from django.db import models
from django.utils.text import slugify


class Stats(models.Model):
    title = models.CharField(max_length=200, unique=True)
    value = models.IntegerField()
    slug = models.SlugField(max_length=200, unique=True)  # descriptive url for the object used in Retrieve API

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Statistics"
        verbose_name = "Statistics"

    def save(self, *args, **kwargs):  # to create slug from title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
