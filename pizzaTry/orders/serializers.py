from django.contrib.auth.models import User
from rest_framework import serializers, permissions
from .models import Order, Pizza, OrderItem




class PizzaSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='order.customer.username')

    class Meta:
        model = Pizza
        fields = ["id", "created", "customer", "type"]


class OrderItemSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(read_only=True)
    id=serializers.ReadOnlyField(source='pizza.id')
    type=serializers.ReadOnlyField(source='pizza.type')


    class Meta:
        model = OrderItem
        fields = ["id", "type", "order", "pizza", "size", "quantity"]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "customer", "status",  "created", "order_items"]

    def get_order_items(self, obj):
        qset = OrderItem.objects.filter(order=obj)
        return [OrderItemSerializer(m).data for m in qset]

class UserSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']