# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genepoum', '0005_auto_20170513_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_qui',
            name='event_qui_comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event_qui',
            name='event_qui_fonction',
            field=models.CharField(default='pere', max_length=100),
            preserve_default=False,
        ),
    ]
