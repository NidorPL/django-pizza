from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = ["id", "customer", "title"]

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, view_name="order-detail", read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']