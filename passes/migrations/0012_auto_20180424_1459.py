# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-24 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0011_auto_20180418_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass',
            name='color',
            field=models.IntegerField(blank=True),
        ),
    ]
