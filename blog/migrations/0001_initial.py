# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 16:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0017_auto_20160910_2216'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=300)),
                ('likes', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_number', models.IntegerField(unique=True)),
                ('vocabulary', models.TextField()),
                ('story', models.TextField()),
                ('cultural_notes', models.TextField()),
                ('action', models.TextField()),
                ('communicaton_skills', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['lesson_number'],
            },
        ),
        migrations.CreateModel(
            name='ImagePostPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', pyuploadcare.dj.models.ImageField(blank=True, verbose_name='Постер(не обязательно)')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('user_id', models.PositiveIntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='NewsProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField(max_length=120, verbose_name='Что у вас нового?')),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 9, 11, 16, 18, 19, 764940, tzinfo=utc))),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Offtop_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('likes', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Заголовок')),
                ('about', models.CharField(max_length=40, verbose_name='Описание')),
                ('message', models.TextField(verbose_name='Текст')),
                ('likes_post', models.IntegerField(default=0)),
                ('heigth_field', models.IntegerField(default=0, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='UserProf',
            fields=[
                ('avatar', pyuploadcare.dj.models.ImageField(blank=True, null=True, verbose_name='Аватар')),
                ('user_key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rank_name', models.CharField(default='НОУНЕЙМ', max_length=10)),
            ],
            options={
                'ordering': ['-user_key'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='offtop_comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newsprofile',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserProf'),
        ),
        migrations.AddField(
            model_name='imagepostpicture',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='img_post', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
