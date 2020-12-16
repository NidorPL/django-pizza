from django.contrib.auth.models import User
from rest_framework import serializers, permissions
from .models import Order, Pizza




class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Order
        fields = ["id", "customer", "title", "status", "pizzas", "created"]


class PizzaSerializer(serializers.ModelSerializer):
    order = serializers.HyperlinkedRelatedField(view_name="order-detail", read_only=True,)

    class Meta:
        model = Pizza
        fields = ["created", "size", "flavour", "order", "quantity"]


class UserSerializer(serializers.ModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, view_name="order-detail", read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']