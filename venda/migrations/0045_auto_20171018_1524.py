# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-18 18:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0044_auto_20171018_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data_pagamento',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 10, 18, 15, 24, 52, 564474)),
        ),
    ]