# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-25 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0012_auto_20180424_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pass',
            old_name='transferable',
            new_name='transferrable',
        ),
    ]
