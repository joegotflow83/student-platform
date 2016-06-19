# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_announcement__class'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('file_upload', models.FileField(upload_to='files/')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Class')),
            ],
        ),
    ]
