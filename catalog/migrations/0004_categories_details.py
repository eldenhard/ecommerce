# Generated by Django 4.2.4 on 2023-09-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='details',
            field=models.ManyToManyField(related_name='categories', to='catalog.details', verbose_name='Характеристики'),
        ),
    ]
