from django.db import models
from django.utils.text import slugify


class Society(models.Model):
    upload_to = "images/society/"
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)
    logo = models.ImageField(upload_to=upload_to)
    slug = models.SlugField(max_length=100, editable=False)

    class Meta:
        verbose_name_plural = "Societies"

    def save(self, *args, **kwargs):  # to create slug from title
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
