# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-29 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanagementsystemapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='user_password',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
