# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20160615_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='credits',
            new_name='credit',
        ),
    ]