# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-12 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='media/image/'),
        ),
    ]