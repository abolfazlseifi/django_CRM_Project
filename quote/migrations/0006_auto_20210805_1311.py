# Generated by Django 3.2.5 on 2021-08-05 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0005_followup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='followup',
            options={'verbose_name': 'پیگیری', 'verbose_name_plural': 'پیگیری ها'},
        ),
        migrations.AlterModelOptions(
            name='quoteitem',
            options={'verbose_name': 'پیش فاکتور', 'verbose_name_plural': 'پیش فاکتورها'},
        ),
    ]
