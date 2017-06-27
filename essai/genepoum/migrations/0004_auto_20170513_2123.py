# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genepoum', '0003_auto_20170513_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateTimeField()),
                ('event_type', models.CharField(choices=[('N', 'Naissance'), ('B', 'Bapt\xe8me'), ('M', 'Mariage'), ('D', 'D\xe9c\xe8s'), ('S', 'S\xe9pulture'), ('X', 'Autre')], default='X', max_length=1)),
                ('event_comment', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='individu',
            name='individu_event',
            field=models.ManyToManyField(blank=True, to='genepoum.Event'),
        ),
    ]