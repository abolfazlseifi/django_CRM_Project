# Generated by Django 3.2.5 on 2021-07-29 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_product', '0003_remove_product_machine'),
        ('organization_machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationmachin',
            options={'verbose_name': 'ماشین', 'verbose_name_plural': 'ماشین آلات'},
        ),
        migrations.AddField(
            model_name='organizationmachin',
            name='active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='فعال / غیر فعال'),
        ),
        migrations.AddField(
            model_name='organizationmachin',
            name='products',
            field=models.ManyToManyField(blank=True, to='organization_product.Product', verbose_name='محصولات'),
        ),
        migrations.AddField(
            model_name='organizationmachin',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='عنوان در url'),
        ),
        migrations.AddField(
            model_name='organizationmachin',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AddField(
            model_name='organizationmachin',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='اسم ماشین '),
        ),
    ]
