# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_announcement_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Class'),
            preserve_default=False,
        ),
    ]
