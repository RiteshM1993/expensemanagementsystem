# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-24 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanagementsystemapp', '0006_auto_20180924_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='upload_imgae',
            new_name='upload_image',
        ),
    ]
