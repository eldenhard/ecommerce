# Generated by Django 4.2.6 on 2023-10-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_alter_products_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Описание'),
        ),
    ]
