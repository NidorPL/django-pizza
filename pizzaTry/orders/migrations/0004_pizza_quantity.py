# Generated by Django 3.1.4 on 2020-12-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20201216_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]