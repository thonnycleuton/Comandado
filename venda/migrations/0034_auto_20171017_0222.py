# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 05:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0033_auto_20171017_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data_pagamento',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 10, 17, 2, 22, 39, 762224)),
        ),
        migrations.AlterField(
            model_name='venda',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'A vista'), (2, 'Prazo'), (3, 'Debito'), (4, 'Credito')]),
        ),
    ]
