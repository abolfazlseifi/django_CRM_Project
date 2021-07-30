# Generated by Django 3.2.5 on 2021-07-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210729_1333'),
        ('product_category', '0003_remove_productcategory_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='product',
            field=models.ManyToManyField(blank=True, to='product.Product', verbose_name='محصولات'),
        ),
    ]