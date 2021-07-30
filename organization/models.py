from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from django.core.validators import RegexValidator


email_regex = RegexValidator(regex='/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{1,3})$/',message='ایمیل شما معتبر نیست')
mobile_regex = RegexValidator(regex='(\+98|0)?9\d{9})',message='موبایل شما معتبر نمی باشد')
phone_regex = RegexValidator(regex='^((?:\+98|0)(\d){2}(\d){8})$',message='تلفن شما معتبر نمی باشد')

class OrganizationProduct(models.Model):
    name = models.CharField(max_length=50,verbose_name='محصولات تولیدی کارفرما')
    class Meta:
        verbose_name = 'محصول تولیدی'
        verbose_name_plural = 'محصولات تولیدی'

    def __str__(self):
        return self.name


class Organization(models.Model):
    province_name = models.CharField(max_length=20, verbose_name='استان')
    organization_name = models.CharField(max_length=50, verbose_name='نام سازمان')
    organization_phone = models.CharField(max_length=11, verbose_name='شماره تلفن سازمان', unique=True)
    organization_staff = models.PositiveIntegerField(verbose_name='تعداد کارگران')
    manufactured_product = models.ManyToManyField(OrganizationProduct, verbose_name='محصولات تولیدی')
    personnel_name = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی کارفرما")
    personnel_mobile = models.CharField(max_length=11, verbose_name='موبایل کارفرما', unique=True)
    personnel_email = models.EmailField(verbose_name='ایمیل کارفرما', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    creator = models.ForeignKey(get_user_model(), verbose_name='کاربر ثبت کننده', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'سازمان'
        verbose_name_plural = 'سازمانها'

    def __str__(self):
        return self.organization_name

