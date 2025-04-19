from rest_framework import serializers
from .models import *


# category model serializer

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'slug']


# product model serializer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        read_only=True
    )

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'slug', 'description', 'price', 'inventory', 'is_active', 'category']


# customer model serializer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()  # shows username

    class Meta:
        model = Customer
        fields = ['url', 'id', 'user', 'phone', 'address', 'joined_at']


# order item model serializer

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name='product-detail',
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['url', 'id', 'product', 'quantity', 'price']


# order model serializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.HyperlinkedRelatedField(
        view_name='customer-detail',
        read_only=True
    )
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['url', 'id', 'customer', 'created_at', 'status', 'total_price', 'items']

