# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0004_auto_20170827_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='comanda',
            field=models.BooleanField(default=True),
        ),
    ]
