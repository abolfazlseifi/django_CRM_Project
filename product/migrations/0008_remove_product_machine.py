# Generated by Django 3.2.5 on 2021-07-30 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='machine',
        ),
    ]
