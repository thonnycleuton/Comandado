# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 06:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0054_auto_20171023_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data_pagamento',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 10, 23, 3, 6, 58, 379433)),
        ),
    ]