# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160930_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviesblog',
            name='user',
        ),
        migrations.DeleteModel(
            name='MoviesBlog',
        ),
    ]