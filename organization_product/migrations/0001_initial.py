# Generated by Django 3.2.5 on 2021-07-28 07:13

from django.db import migrations, models
import organization_product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization_product_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, null=True, upload_to=organization_product.models.upload_image_path, verbose_name='تصویر')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('categories', models.ManyToManyField(blank=True, to='organization_product_category.ProductCategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
