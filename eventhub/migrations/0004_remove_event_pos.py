# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 22:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventhub', '0003_auto_20170318_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='pos',
        ),
    ]