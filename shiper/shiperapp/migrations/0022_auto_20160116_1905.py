# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 12:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0021_auto_20160116_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 12, 5, 2, 343947, tzinfo=utc), editable=False),
        ),
    ]