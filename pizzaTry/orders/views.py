from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, PizzaSerializer
from .models import Order, Pizza
from .serializers import OrderSerializer
from django.db.models import Q




# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format)
    })


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        open_order = Order.objects.filter(Q(customer=self.request.user) & (Q(status=Order.STATUS_OPEN) | Q(status=Order.STATUS_ORDERED)))

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
        print(self.request.data)
        data = self.request.data

        print(1)
        print(data)
        print(data["size"])

        # try to get the same pizza

        open_order = Order.objects.filter(customer=self.request.user, status=Order.STATUS_OPEN).order_by('id').first()

        if not open_order:
            raise APIException("no open order !")

        pizza_already_in_order = Pizza.objects.filter(order=open_order.id).filter(size=data["size"], flavour=data["flavour"])

        if pizza_already_in_order:
            raise APIException("Pizza is already in order")

        serializer.save(order=open_order)

    def perform_update(self, serializer):
        open_order = Order.objects.filter(customer=self.request.user, status=Order.STATUS_OPEN).order_by('id').first()

        if not open_order:
            raise APIException("order cannot be changed anymore !")






