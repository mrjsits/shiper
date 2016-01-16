# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 16:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shiperapp', '0057_auto_20160116_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='code',
            new_name='shipcode',
        ),
        migrations.AlterField(
            model_name='info',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 16, 54, 54, 716895, tzinfo=utc), editable=False),
        ),
    ]
