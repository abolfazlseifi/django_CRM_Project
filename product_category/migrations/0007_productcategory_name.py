# Generated by Django 3.2.5 on 2021-07-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0006_remove_productcategory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=150, null=True, verbose_name='عنوان در URL'),
        ),
    ]
