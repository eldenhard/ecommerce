# Generated by Django 4.2.4 on 2023-09-10 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='OrderItems',
        ),
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]
