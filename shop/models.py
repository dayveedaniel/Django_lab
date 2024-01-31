# Create your models here.

from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField("ID", primary_key=True)
    email = models.EmailField("E-mail", max_length=128)
    first_name = models.CharField("First Name", max_length=128)
    last_name = models.CharField("Last Name", max_length=128)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Order(models.Model):
    order_id = models.AutoField("ID", primary_key=True)
    product = models.CharField("Product", max_length=128)
    order_date = models.DateField("Order Date")
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.order_id, self.product)


# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='products')
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('name',)
#         index_together = (('id', 'slug'),)
#
#     def __str__(self):
#         return self.name
