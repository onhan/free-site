# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-04 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20161011_0201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name']},
        ),
    ]
