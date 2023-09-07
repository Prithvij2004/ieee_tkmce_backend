from django.db import models


class Team(models.Model):
    year = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.year


class TeamMember(models.Model):
    upload_to = "images/team/"
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    rank = models.IntegerField()
    image = models.ImageField(upload_to=upload_to)
    linkedin = models.URLField(max_length=200, blank=True)
    mail_id = models.EmailField(max_length=200)
    member = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")

    class Meta:
        verbose_name_plural = "Team Members"
        verbose_name = "Team Member"
        ordering = ["rank"]

    def __str__(self):
        return self.name
