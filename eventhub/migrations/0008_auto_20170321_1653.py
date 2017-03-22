# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 16:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventhub', '0007_auto_20170320_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.AddField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 21, 16, 53, 34, 155618)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='desc',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='pos',
            field=models.CharField(default='Glasgow', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='preferences',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]