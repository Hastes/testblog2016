# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_likes_dislike'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotesTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotes', models.CharField(max_length=300)),
            ],
        ),
    ]