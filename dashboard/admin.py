from django.contrib import admin

from .models import Class, Schedule


admin.site.register([Class, Schedule])
