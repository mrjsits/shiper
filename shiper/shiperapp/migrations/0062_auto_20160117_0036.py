# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 17:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0061_auto_20160117_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 17, 36, 41, 222031, tzinfo=utc), editable=False),
        ),
    ]
