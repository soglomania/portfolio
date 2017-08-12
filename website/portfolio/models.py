from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=10)
    icon = models.TextField()
    summary = models.TextField()
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

