# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-02 14:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(null=True, upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 14, 14, 9, 448000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 14, 14, 9, 448000, tzinfo=utc)),
        ),
    ]