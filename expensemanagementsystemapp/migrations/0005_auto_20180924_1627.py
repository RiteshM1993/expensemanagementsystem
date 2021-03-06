# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-24 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanagementsystemapp', '0004_uploadpdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('expense_id', models.AutoField(primary_key=True, serialize=False)),
                ('expense_name', models.CharField(max_length=4000)),
                ('total_price', models.BigIntegerField(max_length=4000)),
                ('upload_imgae', models.CharField(max_length=4000)),
                ('created_date', models.DateField(null=True)),
                ('modified_date', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='uploadpdf',
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='modified_date',
            field=models.DateField(null=True),
        ),
    ]
