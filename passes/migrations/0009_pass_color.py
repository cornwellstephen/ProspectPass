# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-17 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0008_auto_20180417_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='pass',
            name='color',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
