# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 13:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160826_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprof',
            name='id',
        ),
        migrations.AlterField(
            model_name='userprof',
            name='user_key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]