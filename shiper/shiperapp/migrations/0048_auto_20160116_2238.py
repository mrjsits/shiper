# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 15:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0047_auto_20160116_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 15, 38, 22, 100846, tzinfo=utc), editable=False),
        ),
    ]