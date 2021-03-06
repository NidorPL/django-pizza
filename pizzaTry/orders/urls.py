from .views import OrderViewSet, UserViewSet, PizzaViewSet, api_root, OrderItemViewSet
from rest_framework import renderers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

order_item_list = OrderItemViewSet.as_view({
    'get': 'list',
    'post': "'create"
})

order_item_detail = OrderItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

pizza_list = PizzaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

pizza_detail = PizzaViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})


router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'order_items', views.OrderItemViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'pizzas', views.PizzaViewSet)


urlpatterns = [
    path('', include(router.urls))
]