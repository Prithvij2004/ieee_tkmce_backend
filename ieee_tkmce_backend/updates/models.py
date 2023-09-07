from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    slug = models.SlugField(max_length=250, unique=True, blank=True, editable=False)
    category = ArrayField(models.CharField(max_length=10, blank=True), size=2, blank=True)

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super().save(*args, **kwargs)


class Image(models.Model):
    upload_loc = "images/updates/"
    image = models.ImageField(upload_to=upload_loc)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="pix")
    name = models.SlugField(default="name", max_length=150)

    def __str__(self):
        return self.image.name.replace(self.upload_loc, "")

    def save(self, *args, **kwargs):
        self.name = settings.MEDIA_URL + self.upload_loc + self.image.name
        super().save(*args, **kwargs)

    def get_some(self):
        self.objects.get(pk=1)
