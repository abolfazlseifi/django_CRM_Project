# Generated by Django 3.2.5 on 2021-08-06 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_alter_organization_personnel_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='organization_phone',
            field=models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن سازمان'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='personnel_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='ایمیل کارفرما'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='personnel_mobile',
            field=models.CharField(max_length=11, verbose_name='موبایل کارفرما'),
        ),
    ]
