# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20160616_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gpa',
        ),
        migrations.AddField(
            model_name='student',
            name='letter',
            field=models.CharField(default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(default=100),
        ),
    ]
