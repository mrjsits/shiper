# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 11:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0019_auto_20160116_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 11, 58, 54, 600718, tzinfo=utc), editable=False),
        ),
    ]
