# Generated by Django 3.2.5 on 2021-08-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0009_auto_20210730_1152'),
        ('product', '0008_remove_product_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='organizationproduct',
            field=models.ManyToManyField(blank=True, to='organization.OrganizationProduct', verbose_name='محصولات کارفرما'),
        ),
    ]
