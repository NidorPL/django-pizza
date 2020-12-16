# Generated by Django 3.1.4 on 2020-12-16 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20201216_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='title',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='orders.order'),
        ),
    ]
