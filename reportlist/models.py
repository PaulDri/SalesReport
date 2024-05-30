import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class SalesReport(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=50, default="")
    product_category = models.CharField(max_length=50)
    product_sold = models.IntegerField()
    product_sales = models.DecimalField(decimal_places=2, max_digits=10000)
    total_quantity = models.IntegerField()
    total_sales = models.DecimalField(decimal_places=2, max_digits=10000)
    avg_order_value = models.DecimalField(decimal_places=2, max_digits=100000)
    sales_percentage = models.DecimalField(decimal_places=2, max_digits=10000)
    monthly_sales = models.DecimalField(decimal_places=2, max_digits=10000)
