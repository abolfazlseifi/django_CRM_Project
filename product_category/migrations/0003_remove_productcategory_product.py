# Generated by Django 3.2.5 on 2021-07-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0002_productcategory_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='product',
        ),
    ]
