# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datafreezer', '0005_auto_20160810_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]
