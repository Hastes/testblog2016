# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20161001_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentformoveis',
            name='movie_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_movies', to='movies.MoviesBlog'),
        ),
    ]
