# Generated by Django 3.2.5 on 2021-07-29 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization_product', '0002_product_machine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='machine',
        ),
    ]
