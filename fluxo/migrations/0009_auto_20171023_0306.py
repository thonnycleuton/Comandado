# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fluxo', '0008_auto_20171023_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='vencimento',
            field=models.PositiveIntegerField(help_text='Dia do mes para um vencimento fixo'),
        ),
    ]