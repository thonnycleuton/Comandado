# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-27 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='cod_cliente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]
