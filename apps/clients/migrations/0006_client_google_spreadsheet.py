# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_client_is_custom'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='google_spreadsheet',
            field=models.URLField(blank=True, null=True, verbose_name='Google spreadsheet SQR'),
        ),
    ]
