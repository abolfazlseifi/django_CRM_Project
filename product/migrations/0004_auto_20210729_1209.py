# Generated by Django 3.2.5 on 2021-07-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_remove_organizationmachin_products'),
        ('product', '0003_remove_product_machine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='machine',
            field=models.ManyToManyField(blank=True, to='organization.OrganizationMachin', verbose_name='ماشین های مورد نیاز'),
        ),
    ]
