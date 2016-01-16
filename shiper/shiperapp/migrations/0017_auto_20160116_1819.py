# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 11:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0016_auto_20160116_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 11, 19, 41, 224719, tzinfo=utc)),
        ),
    ]