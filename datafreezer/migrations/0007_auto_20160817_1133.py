# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datafreezer', '0006_auto_20160817_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='_title',
            field=models.CharField(blank=True, db_column=b'title', max_length=500, null=True),
        ),
    ]