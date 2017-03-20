# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventhub', '0006_auto_20170318_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='pos',
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(default=1111111111, on_delete=django.db.models.deletion.CASCADE, to='eventhub.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(default='date', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(default='date', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(default='cat', max_length=32),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]