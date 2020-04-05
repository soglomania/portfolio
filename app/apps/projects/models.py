from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.TextField()
    summary = models.TextField()
    description = models.TextField()
    category = models.TextField()

    logo = models.TextField()
    github = models.URLField()
    link = models.URLField()


    def __str__(self):
        return self.title



