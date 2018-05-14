# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('querystring', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoryAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=128)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story')),
            ],
        ),
        migrations.AddField(
            model_name='query',
            name='attribute',
            field=models.ManyToManyField(to='stories.StoryAttribute'),
        ),
        migrations.AddField(
            model_name='query',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story'),
        ),
    ]
