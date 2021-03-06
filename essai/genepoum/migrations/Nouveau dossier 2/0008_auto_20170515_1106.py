# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genepoum', '0007_individu_individu_sexe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individu',
            name='individu_mere',
        ),
        migrations.AddField(
            model_name='individu',
            name='individu_mere',
            field=models.ForeignKey(blank=True, default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='mere', to='genepoum.Individu'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='individu',
            name='individu_pere',
        ),
        migrations.AddField(
            model_name='individu',
            name='individu_pere',
            field=models.ForeignKey(blank=True, default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='pere', to='genepoum.Individu'),
            preserve_default=False,
        ),
    ]
