# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 12:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0113_auto_20160118_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 12, 13, 57, 661422, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 12, 13, 57, 661422, tzinfo=utc), editable=False),
        ),
    ]
