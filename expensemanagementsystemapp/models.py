# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class registeruser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=4000)
    user_email = models.CharField(max_length=4000)
    created_date = models.DateField(null=True)
    modified_date = models.DateField(null=True)
    user_password = models.CharField(max_length=4000, null=True)

    class Meta:
        db_table = "register_user"

class expenses(models.Model):
    expense_id = models.AutoField(primary_key=True)
    expense_name= models.CharField(max_length=4000)
    total_price = models.BigIntegerField(max_length=4000)
    upload_image = models.CharField(max_length=4000)
    created_date = models.DateField(null=True)
    modified_date = models.DateField(null=True)

    class Meta:
        db_table = "expenses"

