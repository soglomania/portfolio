from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=250)
    icon = models.ImageField()
    summary = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return self.title

