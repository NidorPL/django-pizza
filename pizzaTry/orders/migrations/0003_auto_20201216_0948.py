# Generated by Django 3.1.4 on 2020-12-16 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201211_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
