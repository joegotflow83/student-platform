from django.contrib import admin

from .models import Class, Schedule, Student, Announcement, File


admin.site.register([Class, Schedule, Student, Announcement, File])
