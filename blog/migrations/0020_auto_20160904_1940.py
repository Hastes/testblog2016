# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_english'),
    ]

    operations = [
        migrations.AlterField(
            model_name='english',
            name='lesson_number',
            field=models.IntegerField(unique=True),
        ),
    ]