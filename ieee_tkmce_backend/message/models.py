from django.db import models


class Message(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
