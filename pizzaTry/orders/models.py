from django.db import models
from django_fsm import FSMField, transition, FSMIntegerField


PIZZA_FLAVOURS = [('MARGARIHA', "Margarita"), ("MARGINARA", "Marginara"), ("SALAMI", "Salami")]
PIZZA_SIZES = [("SMALL", "small"), ("MEDIUM", "medium"), ("LARGE", "large")]


class Order(models.Model):
    STATUS_CREATED = 0
    STATUS_PAID = 1
    STATUS_FULFILLED = 2
    STATUS_CANCELLED = 3
    STATUS_RETURNED = 4
    STATUS_CHOICES = (
        (STATUS_CREATED, 'created'),
        (STATUS_PAID, 'paid'),
        (STATUS_FULFILLED, 'fulfilled'),
        (STATUS_CANCELLED, 'cancelled'),
        (STATUS_RETURNED, 'returned'),
    )
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    status = FSMIntegerField(choices=STATUS_CHOICES, default=STATUS_CREATED, protected=True)



    class Meta:
        ordering = ['created']

    @transition(field=status, source=STATUS_CREATED, target=STATUS_PAID)
    def pay(self, amount):
        print("calling pay method")
        self.amount = amount
        print("Pay amount {} for the order".format(self.amount))
    @transition(field=status, source=STATUS_PAID, target=STATUS_FULFILLED)
    def fulfill(self):
        print("Fulfill the order")
    @transition(field=status, source=[STATUS_CREATED, STATUS_PAID], target=STATUS_CANCELLED)
    def cancel(self):
        print("Cancel the order")
    @transition(field=status, source=STATUS_FULFILLED, target=STATUS_RETURNED)
    def _return(self):
        print("Return the order")

    def __str__(self):
        return "%s %s" % (self.title, self.customer)


class Pizza(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default="")
    created = models.DateTimeField(auto_now_add=True)
    size = models.CharField(choices=PIZZA_SIZES, max_length= 100)
    flavour = models.CharField(choices=PIZZA_FLAVOURS, max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s" % (self.flavour, self.size)

    class Meta:
        ordering = ['created']
