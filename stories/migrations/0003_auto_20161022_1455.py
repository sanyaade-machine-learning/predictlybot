# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 14:55
from __future__ import unicode_literals

import annoying.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_query_configured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='attribute',
            new_name='attributes',
        ),
        migrations.AddField(
            model_name='query',
            name='parsed_ner',
            field=annoying.fields.JSONField(blank=True, null=True),
        ),
    ]