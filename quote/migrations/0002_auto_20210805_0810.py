# Generated by Django 3.2.5 on 2021-08-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quoteemailhistory',
            old_name='was_successfull',
            new_name='sent_email',
        ),
        migrations.RemoveField(
            model_name='quotefollowup',
            name='content',
        ),
        migrations.AddField(
            model_name='quotefollowup',
            name='text',
            field=models.TextField(default=None, verbose_name='متن پیگیری'),
        ),
    ]