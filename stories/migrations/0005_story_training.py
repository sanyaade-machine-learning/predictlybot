# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_remove_query_attributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='training',
            field=models.BooleanField(default=False),
        ),
    ]
