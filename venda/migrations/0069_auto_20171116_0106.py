# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 04:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0068_auto_20171116_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data_pagamento',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 16, 1, 6, 52, 853544)),
        ),
    ]