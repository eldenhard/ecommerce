# Generated by Django 4.2.4 on 2023-09-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_orderitems_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='rate',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Курс к ₽'),
        ),
    ]
