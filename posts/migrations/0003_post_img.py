# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20171105_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
    ]