# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqr', '0007_auto_20171005_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='is_cities',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='is_countries',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='is_states',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]