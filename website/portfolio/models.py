from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=10)
    icon = models.ImageField()
    summary = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return self.title

