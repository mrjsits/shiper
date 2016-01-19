# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 04:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0140_auto_20160119_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 4, 21, 4, 754414, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='info',
            name='reciever',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='info',
            name='reciever_address',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='info',
            name='reciever_phone',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 4, 21, 4, 770038, tzinfo=utc), editable=False),
        ),
    ]