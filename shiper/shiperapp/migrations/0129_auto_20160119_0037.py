# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 17:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shiperapp', '0128_auto_20160119_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='username',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 17, 37, 43, 739921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 17, 37, 43, 739921, tzinfo=utc), editable=False),
        ),
    ]