# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluxo', '0012_auto_20171030_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor'),
        ),
    ]
