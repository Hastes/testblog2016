# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 04:29
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprof',
            name='avatar',
            field=pyuploadcare.dj.models.ImageField(null=True, verbose_name='Аватар'),
        ),
    ]