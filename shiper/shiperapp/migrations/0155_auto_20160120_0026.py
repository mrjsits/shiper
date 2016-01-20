# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 17:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0154_auto_20160120_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 17, 26, 50, 363052, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 17, 26, 50, 363052, tzinfo=utc), editable=False),
        ),
    ]
