# Generated by Django 4.2.6 on 2023-10-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_brands_image_link_categories_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.TextField(db_index=True, verbose_name='Название'),
        ),
    ]
