# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 11:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0111_auto_20160118_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 11, 34, 41, 505723, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 11, 34, 41, 505723, tzinfo=utc)),
        ),
    ]
