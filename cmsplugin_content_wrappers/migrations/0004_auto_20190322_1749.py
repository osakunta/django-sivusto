# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-22 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_content_wrappers', '0003_contentcolumn'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentarea',
            name='extra_classes',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='contentsection',
            name='extra_classes',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
