# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-12 08:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appone', '0004_auto_20180512_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=200)),
                ('usr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
