from django.db import models
from django_fsm import FSMField, transition, FSMIntegerField


PIZZA_FLAVOURS = [('MARGARIHA', "Margarita"), ("MARGINARA", "Marginara"), ("SALAMI", "Salami")]
PIZZA_SIZES = [("SMALL", "small"), ("MEDIUM", "medium"), ("LARGE", "large")]


class Order(models.Model):
    STATUS_OPEN = 0
    STATUS_ORDERED = 1
    STATUS_IN_DELIVERY = 2
    STATUS_DELIVERED = 3
    STATUS_CANCELLED = 4

    # Die Status würde ich eig in einem extra file, zB constants.py speichern und hier nur importieren wollen

    STATUS_CHOICES = (
        (STATUS_OPEN, 'open'),
        (STATUS_ORDERED, 'ordered'),
        (STATUS_IN_DELIVERY, 'in_delivery'),
        (STATUS_DELIVERED, 'delivered'),
        (STATUS_CANCELLED, 'cancelled'),
    )
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    status = FSMIntegerField(choices=STATUS_CHOICES, default=STATUS_OPEN)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return "%s %s" % (self.title, self.customer)


class Pizza(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="pizzas", default="")
    created = models.DateTimeField(auto_now_add=True)
    size = models.CharField(choices=PIZZA_SIZES, max_length= 100)
    flavour = models.CharField(choices=PIZZA_FLAVOURS, max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s" % (self.flavour, self.size)

    class Meta:
        ordering = ['created']
