# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-updated'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
