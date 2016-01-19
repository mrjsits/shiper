# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 03:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0139_auto_20160119_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 3, 35, 41, 112741, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 3, 35, 41, 112741, tzinfo=utc), editable=False),
        ),
    ]