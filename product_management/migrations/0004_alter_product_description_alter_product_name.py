# Generated by Django 4.1.6 on 2023-07-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0003_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
