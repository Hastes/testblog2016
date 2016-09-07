# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 16:00
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20160828_2114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprof',
            options={'ordering': ['-user_key']},
        ),
        migrations.AlterField(
            model_name='userprof',
            name='avatar',
            field=models.ImageField(blank=True, height_field='heigth_field', null=True, upload_to=blog.models.upload_url_for_user, validators=[blog.models.UserProf.validate_image], verbose_name='Постер', width_field='width_field'),
        ),
    ]