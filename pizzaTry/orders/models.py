from django.db import models
from django_fsm import FSMField, transition, FSMIntegerField


PIZZA_FLAVOURS = [('MARGARIHA', "Margarita"), ("MARGINARA", "Marginara"), ("SALAMI", "Salami")]


class Pizza(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=PIZZA_FLAVOURS, max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['created']


class Order(models.Model):
    STATUS_OPEN = 0
    STATUS_ORDERED = 1
    STATUS_IN_DELIVERY = 2
    STATUS_DELIVERED = 3
    STATUS_CANCELLED = 4

    STATUS_CHOICES = (
        (STATUS_OPEN, 'open'),
        (STATUS_ORDERED, 'ordered'),
        (STATUS_IN_DELIVERY, 'in_delivery'),
        (STATUS_DELIVERED, 'delivered'),
        (STATUS_CANCELLED, 'cancelled'),
    )
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    status = FSMIntegerField(choices=STATUS_CHOICES, default=STATUS_OPEN)
    order_items = models.ManyToManyField(Pizza, through='OrderItem')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "%s %s" % (self.id, self.customer)


class OrderItem(models.Model):
    SIZE_SMALL = "SMALL"
    SIZE_MEDIUM = "MEDIUM"
    SIZE_LARGE = "LARGE"
    PIZZA_SIZES = ((SIZE_SMALL, 'small'), (SIZE_MEDIUM, 'medium'), (SIZE_LARGE, 'large'))

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(choices=PIZZA_SIZES, max_length=50)
    quantity = models.IntegerField()





