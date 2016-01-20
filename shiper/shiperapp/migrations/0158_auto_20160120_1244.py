# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 05:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0157_auto_20160120_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 5, 44, 40, 352272, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 5, 44, 40, 353274, tzinfo=utc), editable=False),
        ),
    ]
