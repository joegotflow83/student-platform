from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=64)
    level = models.IntegerField()
    credits = models.IntegerField()
    location = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
