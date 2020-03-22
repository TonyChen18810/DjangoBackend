# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('adwords_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='AdWords ID')),
                ('bingads_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='BingAds ID')),
                ('facebookads_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook Ads ID')),
                ('is_enabled', models.BooleanField(default=False)),
                ('master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='clients.Client', verbose_name='Master')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]