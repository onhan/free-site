# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-06 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0039_auto_20161106_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commission',
            options={'ordering': ['author', 'article']},
        ),
        migrations.RemoveField(
            model_name='commission',
            name='date_notified_processed',
        ),
        migrations.RemoveField(
            model_name='commission',
            name='date_processed',
        ),
        migrations.RemoveField(
            model_name='commission',
            name='date_rejected',
        ),
        migrations.RemoveField(
            model_name='commission',
            name='our_reference',
        ),
        migrations.RemoveField(
            model_name='commission',
            name='their_reference',
        ),
        migrations.AddField(
            model_name='commission',
            name='vatable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invoice',
            name='our_reference',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='invoice',
            name='their_reference',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='commission',
            name='fund',
            field=models.ForeignKey(blank=True, help_text='Selecting a fund approves the commission', null=True, on_delete=django.db.models.deletion.CASCADE, to='newsroom.Fund'),
        ),
    ]
