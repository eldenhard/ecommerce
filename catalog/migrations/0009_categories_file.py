# Generated by Django 4.2.4 on 2023-09-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_categories_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='Лого'),
        ),
    ]
