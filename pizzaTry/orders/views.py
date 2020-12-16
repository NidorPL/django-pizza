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
        serializer.save(customer=self.request.user)

    def perform_update(self, serializer):
        print("updating in view")

        print(self)

        order = self.get_object()

        print(order.status)

        if order.status > 1:
            raise APIException("Order cannot be changed anymore !")

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
        print(1)
        print(self.request)

        # get not completed order of customer OR create one and add this as order


        openorder = Order.objects.filter(customer=self.request.user).order_by('id').first()

        print("open order")

        print(openorder)

        serializer.save(order=openorder)





