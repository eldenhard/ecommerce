# Generated by Django 4.2.6 on 2023-10-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_products_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='Название'),
        ),
    ]
