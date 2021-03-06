# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genepoum', '0010_auto_20170515_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individu',
            name='individu_mere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mere', to='genepoum.Individu'),
        ),
        migrations.AlterField(
            model_name='individu',
            name='individu_pere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pere', to='genepoum.Individu'),
        ),
    ]
