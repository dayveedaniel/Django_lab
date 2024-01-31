# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=512)
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'customers'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=512)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'
