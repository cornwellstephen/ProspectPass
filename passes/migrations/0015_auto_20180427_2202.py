# Generated by Django 2.0.3 on 2018-04-27 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0014_auto_20180427_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='nom',
        ),
    ]
