from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, PizzaSerializer, OrderItemSerializer
from .models import Order, Pizza, OrderItem
from .serializers import OrderSerializer
from django.db.models import Q

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format)
    })


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        status = self.request.query_params.get('status', None)
        customer = self.request.query_params.get('customer', None)

        if status is not None:
            queryset = queryset.filter(status=status)

        if customer is not None:
            queryset = queryset.filter(customer=customer)

        return queryset



    def perform_create(self, serializer):
        open_order = Order.objects.filter(Q(customer=self.request.user), status__in=[Order.STATUS_OPEN, Order.STATUS_ORDERED])

        if open_order:
            raise APIException("you already have an open order")

        serializer.save(customer=self.request.user)

    def perform_update(self, serializer):
        status = self.request.data["status"]
        order = self.get_object()

        if status != order.status:
            if order.status > Order.STATUS_IN_DELIVERY:
                raise APIException("Order is already finalized")

        serializer.save()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        data = self.request.data

        pizza_already_created = Pizza.objects.filter(type=data["type"])

        if pizza_already_created:
            raise APIException("Pizza was already created")

        serializer.save()


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        data = self.request.data

        is_pizza_already_in_order = OrderItem.objects.filter(order_id=data["order"], pizza_id=data["pizza"], size=data["size"])

        if is_pizza_already_in_order:
            raise APIException("Pizza with same size is already in order !")

        serializer.save()

    def perform_update(self, serializer):
        data = self.request.data

        is_pizza_already_in_order = OrderItem.objects.filter(order_id=data["order"], pizza_id=data["pizza"], size=data["size"])

        if is_pizza_already_in_order:
            raise APIException("Pizza with same size is already in order !")





