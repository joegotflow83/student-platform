from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """As in enrolled for a particular class"""
    user = models.ForeignKey(User)
    name_of_class = models.CharField(max_length=64)
    grade = models.IntegerField(default=100)
    letter = models.CharField(max_length=1, default='A')


class Class(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    level = models.IntegerField()
    credits = models.IntegerField()
    location = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    limit = models.IntegerField()
    taken = models.IntegerField(default=0)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    user = models.ForeignKey(User)
    classes = models.ManyToManyField(Class, blank=True)


class Announcement(models.Model):
    user = models.ForeignKey(User)
    _class = models.ForeignKey(Class)
    title = models.CharField(max_length=128)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Quiz(models.Model):
    _class = models.ForeignKey(Class)
    name = models.CharField(max_length=128)
    grade = models.IntegerField()


class Score(models.Model):
    score = models.IntegerField()


class File(models.Model):
    name = models.CharField(max_length=128)
    file_upload = models.FileField(upload_to="files/")
    created = models.DateTimeField(auto_now_add=True)
    _class = models.ForeignKey(Class)
