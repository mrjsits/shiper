# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 12:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0114_auto_20160118_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 12, 22, 44, 872314, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 12, 22, 44, 872314, tzinfo=utc), editable=False),
        ),
    ]
