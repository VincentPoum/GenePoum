# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genepoum', '0006_auto_20170514_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='individu',
            name='individu_sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'F\xe9minin'), ('X', 'Autre')], default='X', max_length=1),
        ),
    ]
