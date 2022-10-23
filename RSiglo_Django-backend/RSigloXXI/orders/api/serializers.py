from dataclasses import field
from itertools import product
from rest_framework.serializers import ModelSerializer

from orders.models import Order
from products.api.serializers import ProductSerializer
from tables.api.serializers import TableSerializer


#detalle del producto y mesa de la orden 
class OrderSerializer(ModelSerializer):
    product_data = ProductSerializer(source='products', read_only=True, many=True)
    table_data = TableSerializer(source='table', read_only=True)

    class Meta:
        model = Order
        fields = ['id','status','table', 'table_data', 'products', 'product_data', 'payment', 'close', 'created_at']

        