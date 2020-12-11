from django.db import models

PIZZA_FLAVOURS = [('MARGARIHA', "Margarita"), ("MARGINARA", "Marginara"), ("SALAMI", "Salami")]
PIZZA_SIZES = [("SMALL", "small"), ("MEDIUM", "medium"), ("LARGE", "large")]


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['created']


class Pizza(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    size = models.CharField(choices=PIZZA_SIZES, max_length= 100)
    flavour = models.CharField(choices=PIZZA_FLAVOURS, max_length=100)
