# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 16:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0054_auto_20160116_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 16, 38, 12, 595556, tzinfo=utc), editable=False),
        ),
    ]
