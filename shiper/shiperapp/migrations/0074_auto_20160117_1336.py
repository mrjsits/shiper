# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 06:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0073_auto_20160117_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 17, 6, 36, 2, 638735, tzinfo=utc), editable=False),
        ),
    ]
