# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170911_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='meta',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]