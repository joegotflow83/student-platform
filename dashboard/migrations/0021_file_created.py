# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 18:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 19, 18, 29, 38, 191330, tzinfo=utc)),
            preserve_default=False,
        ),
    ]