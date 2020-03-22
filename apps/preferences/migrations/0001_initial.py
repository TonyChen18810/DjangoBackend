# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-07 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bing_access_token', models.TextField(blank=True, null=True)),
                ('bing_refresh_token', models.TextField(blank=True, null=True)),
                ('bing_expires_in', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Preferences',
                'db_table': 'preferences',
            },
        ),
    ]
