# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0007_auto_20170201_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='calender',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
