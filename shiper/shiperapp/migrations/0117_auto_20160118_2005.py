# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 13:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0116_auto_20160118_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='address',
        ),
        migrations.RemoveField(
            model_name='info',
            name='name',
        ),
        migrations.RemoveField(
            model_name='info',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='info',
            name='username',
        ),
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 13, 5, 6, 835149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 13, 5, 6, 835149, tzinfo=utc), editable=False),
        ),
    ]
