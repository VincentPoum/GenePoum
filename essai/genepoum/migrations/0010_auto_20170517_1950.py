# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genepoum', '0009_auto_20170516_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.CharField(max_length=40),
        ),
    ]
