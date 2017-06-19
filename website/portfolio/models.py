from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=10)
    icon = models.URLField()
    summary = models.TextField()
    description = models.TextField()
    image = models.URLField()
    link = models.URLField()

    def __str__(self):
        return self.title

