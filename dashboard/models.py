from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    name = models.CharField(max_length=64)
    level = models.IntegerField()
    credit = models.IntegerField()
    location = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    limit = models.IntegerField()
    taken = models.IntegerField()


class Schedule(models.Model):
    user = models.ForeignKey(User)
    classes = models.ManyToManyField(Class, blank=True)
