# Generated by Django 4.2.4 on 2023-09-10 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_orders_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='currency',
        ),
    ]