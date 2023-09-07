from django.db import models
from django.utils.text import slugify


class Award(models.Model):
    upload_loc = "images/awards/"
    HIGH = "HIGH"
    LOW = "LOW"
    CHOICES = (
        (1, HIGH),
        (0, LOW),
    )
    name = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    priority = models.IntegerField(default=0, choices=CHOICES)
    image = models.ImageField(upload_to=upload_loc)
    slug = models.SlugField(max_length=150, blank=True, editable=False, unique=True)
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-priority", "-pub_date"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
