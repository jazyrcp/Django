# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-12 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20180511_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Third',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='second',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]