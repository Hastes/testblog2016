# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20160919_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score2048',
            old_name='score',
            new_name='score_user',
        ),
    ]
