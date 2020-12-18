# Generated by Django 3.1.4 on 2020-12-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20201216_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='pizzas',
            field=models.ManyToManyField(to='orders.Pizza'),
        ),
    ]