# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='date',
        ),
        migrations.AddField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 10, 54, 6, 66837, tzinfo=utc)),
        ),
    ]
