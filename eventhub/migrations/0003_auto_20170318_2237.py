# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventhub', '0002_auto_20170318_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventhub.Category'),
        ),
    ]