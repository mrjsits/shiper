# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 15:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0097_auto_20160117_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 17, 15, 53, 11, 980630, tzinfo=utc), editable=False),
        ),
    ]