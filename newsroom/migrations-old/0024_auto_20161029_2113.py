# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-29 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0023_auto_20161029_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newsroom.Article'),
        ),
        migrations.AlterField(
            model_name='commission',
            name='fund',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newsroom.Fund'),
        ),
    ]
