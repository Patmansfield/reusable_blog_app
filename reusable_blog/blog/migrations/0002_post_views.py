# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reusable_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
