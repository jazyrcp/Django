# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-11 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_second'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]