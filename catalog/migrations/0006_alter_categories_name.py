# Generated by Django 4.2.4 on 2023-09-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_categories_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
