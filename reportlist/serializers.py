from rest_framework import serializers
from .models import SalesReport

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = [
            'date', 'product_category', 'product_sold',
            'product_sales', 'total_quantity', 'total_sales', 'avg_order_value',
            'sales_percentage', 'monthly_sales'
        ]