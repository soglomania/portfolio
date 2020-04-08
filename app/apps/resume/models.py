from django.db import models
from django.utils import timezone
import datetime

class Biography(models.Model):
    
    surname = models.TextField()
    firstname = models.TextField()
    date_of_birth = models.DateField()
    job_title = models.TextField()
    address = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField()
    summary = models.TextField()
    description = models.TextField()
    
    youtube = models.URLField()
    facebook = models.URLField()
    github = models.URLField()
    linkedin = models.URLField()
    viadeo = models.URLField()
    twitter = models.URLField()

    def name(self):
        return "%(firstname)s %(surname)s" %({'firstname' : self.firstname, 'surname' : self.surname })

    def lastname(self):
        return self.surname

    def age(self):
        return (datetime.date.today() - self.date_of_birth).days // 365

    def __str__(self):
        return self.name()


class Language(models.Model):
    
    name = models.TextField()
    start_date = models.DateField()
    level = models.TextField()
    summary = models.TextField()
    description = models.TextField()

    def __str__(self):
        return "{} : {}".format(self.name, self.level)



class Education(models.Model):
    name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    school = models.TextField()
    summary = models.TextField()
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    company = models.TextField()
    summary = models.TextField()
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.TextField()
    summary = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Interest(models.Model):
    
    name = models.TextField()
    summary = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name



