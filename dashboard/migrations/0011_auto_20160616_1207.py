# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20160616_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='dashboard.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='joe@absolutod.com', max_length=254),
            preserve_default=False,
        ),
    ]
