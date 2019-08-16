# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0015_article_freelancer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='freelancer',
        ),
        migrations.AddField(
            model_name='author',
            name='freelancer',
            field=models.BooleanField(default=False),
        ),
    ]
