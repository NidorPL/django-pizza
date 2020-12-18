# Generated by Django 3.1.4 on 2020-12-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20201218_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_pizzas',
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(related_name='order_item', through='orders.OrderItem', to='orders.Pizza'),
        ),
    ]
