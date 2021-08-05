# Generated by Django 3.2.5 on 2021-08-05 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0010_auto_20210801_1623'),
        ('quote', '0004_auto_20210805_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('text', models.TextField(default=None, verbose_name='متن پیگیری')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر ثبت کننده')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization', verbose_name='سازمان')),
            ],
        ),
    ]