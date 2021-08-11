from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum, F, Case, When
from django.core.validators import MinValueValidator, MaxValueValidator


# <--------------------| مدل پیش فاکتور |-------------------->

class Quote(models.Model):
    organization = models.ForeignKey("organization.Organization", on_delete=models.PROTECT, verbose_name="سازمان")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    creator = models.ForeignKey(get_user_model(), verbose_name='کاربر ثبت کننده', on_delete=models.CASCADE)
    tax = 9

    class Meta:
        verbose_name = 'پیش فاکتور'
        verbose_name_plural = 'پیش فاکتورها'

    def __str__(self):
        return f'{self.organization}'

    def get_total_number(self):  # جمع تعداد
        return self.quoteitem_set.all(). \
            aggregate(Sum('number')).get('number__sum', 0)

    def get_total_base_price(self):  # جمع قیمت پایه
        return self.quoteitem_set.all().annotate(total_base_price=F('number') * F('price')) \
            .aggregate(Sum('total_base_price'))['total_base_price__sum']

    def get_quote_discount(self):  # جمع تخفیف ها
        return self.quoteitem_set.all().annotate(
            total_base_price=F('number') * F('price')).annotate(
            total_discount=(F('discount') * F('total_base_price') / 100)) \
            .aggregate(Sum('total_discount'))['total_discount__sum']

    def get_quote_tax(self, tax=tax):  # جمع مالیات
        return self.quoteitem_set.all().annotate(
            total_base_price=F('number') * F('price')).annotate(
            total_price=F('total_base_price') - (F('discount') * F('total_base_price') / 100)).annotate(
            total_tax=Case(
                When(product__tax=True, then=(F('total_price') * tax / 100)),
                When(product__tax=False, then=0),
                output_field=models.PositiveIntegerField()
            )
        ).aggregate(Sum('total_tax'))['total_tax__sum']

    def get_total_price(self, tax=tax):  # جمع کلی
        return self.quoteitem_set.all().annotate(
            total_base_price=F('number') * F('price')).annotate(
            total_price=F('total_base_price') - (F('discount') * F('total_base_price') / 100)).annotate(
            total_price=Case(
                When(product__tax=True, then=F('total_price') + (F('total_price') * tax / 100)),
                When(product__tax=False, then=F('total_price')),
                output_field=models.PositiveIntegerField()
            )
        ).aggregate(Sum('total_price'))['total_price__sum']


# <--------------------| آیتم پیش فاکتور |-------------------->

class QuoteItem(models.Model):
    quote = models.ForeignKey("Quote", on_delete=models.CASCADE, verbose_name='پیش فاکتور')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="محصول")
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    number = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name='تعداد')
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], verbose_name='درصد تخفیف')

    class Meta:
        verbose_name = 'رکورد پیش فاکتور'
        verbose_name_plural = 'رکورد پیش فاکتورها'

    def __str__(self):
        return f'{self.quote} {self.product}'

    def get_total_price(self):
        return self.number * self.price


# <--------------------| تاریخچه ارسال ایمیل |-------------------->

class QuoteEmailHistory(models.Model):
    receiver = models.EmailField(verbose_name="ایمیل گیرنده")
    sent_email = models.BooleanField(default=False, verbose_name="ایمیل ارسال شد؟")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    user_sender = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="کاربر ارسال کننده")

    def __str__(self):
        return self.receiver


# <--------------------| پیگیری |-------------------->

class FollowUp(models.Model):
    organization = models.ForeignKey('organization.Organization', verbose_name="سازمان", on_delete=models.CASCADE)
    creator = models.ForeignKey(get_user_model(), verbose_name='کاربر ثبت کننده', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن پیگیری', default=None)

    class Meta:
        verbose_name = 'پیگیری'
        verbose_name_plural = 'پیگیری ها'
