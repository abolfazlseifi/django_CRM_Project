from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from django.core.validators import RegexValidator

email_regex = RegexValidator(regex='/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{1,3})$/', message='ایمیل شما معتبر نیست')
mobile_regex = RegexValidator(regex='(\+98|0)?9\d{9})', message='موبایل شما معتبر نمی باشد')
phone_regex = RegexValidator(regex='^((?:\+98|0)(\d){2}(\d){8})$', message='تلفن شما معتبر نمی باشد')


class OrganizationProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name='محصولات تولیدی کارفرما')

    class Meta:
        verbose_name = 'محصول تولیدی'
        verbose_name_plural = 'محصولات تولیدی'

    def __str__(self):
        return self.name


    def get_suggest_product(self):
        return [product for product in self.product_set.all()]



class Province(models.Model):
    name = models.CharField(max_length=100, verbose_name="استان", unique=True )

    class Meta():
        verbose_name = "استان"
        verbose_name_plural ="استان ها"

    def __str__(self):
        return self.name

class Organization(models.Model):
    province_name = models.CharField(max_length=20, verbose_name='استان')
    organization_name = models.CharField(max_length=50, verbose_name='نام سازمان')
    organization_phone = models.CharField(validators=[phone_regex],max_length=11, verbose_name='شماره تلفن سازمان', unique=True)
    organization_staff = models.PositiveIntegerField(verbose_name='تعداد کارگران')
    organization_product = models.ManyToManyField(OrganizationProduct, verbose_name='محصولات تولیدی')
    personnel_name = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی کارفرما")
    personnel_mobile = models.CharField(validators=[mobile_regex],max_length=11, verbose_name='موبایل کارفرما', unique=True)
    personnel_email = models.EmailField(validators=[email_regex],verbose_name='ایمیل کارفرما', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    creator = models.ForeignKey(get_user_model(), verbose_name='کاربر ثبت کننده', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['organization_name','creator' ]
        verbose_name = 'سازمان'
        verbose_name_plural = 'سازمانها'

    def __str__(self):
        return self.organization_name

    def get_organization_product(self):
        return [product.name for product in self.organization_product.all()]

    def get_suggest_product(self):
        p = list()
        for product in self.organization_product.all():
            for l in product.get_suggest_product():
                p.append(l.title)
        p = set(p)
        return list(p)
