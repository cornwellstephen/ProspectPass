# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-01 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('netid', models.CharField(max_length=40, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('user_club', models.CharField(max_length=200)),
                ('password', models.TextField()),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='pass',
            name='pass_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes', to='passes.Student'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
