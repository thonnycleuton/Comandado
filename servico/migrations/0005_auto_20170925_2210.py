# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0004_auto_20170909_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='categoria',
            field=models.IntegerField(choices=[(4, 'Depilação'), (5, 'Salão'), (6, 'Estética Facial'), (7, 'Estética Corporal'), (8, 'Manicure')]),
        ),
    ]