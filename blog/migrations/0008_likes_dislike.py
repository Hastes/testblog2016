# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160930_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
    ]
