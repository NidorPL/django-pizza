# Generated by Django 3.1.4 on 2020-12-16 11:07

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_pizza_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(0, 'created'), (1, 'paid'), (2, 'fulfilled'), (3, 'cancelled'), (4, 'returned')], default=0, protected=True),
        ),
    ]