from django.contrib.auth import get_user_model
from django.db import models


class Quote(models.Model):
    organization = models.ForeignKey("organization.Organization", on_delete=models.PROTECT, verbose_name="سازمان")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    creator = models.ForeignKey(get_user_model(), verbose_name='کاربر ثبت کننده', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'پیش فاکتور'
        verbose_name_plural = 'پیش فاکتورها'

    def __str__(self):
        return f'{self.organization}'

    def sum_price(self):
        return self.quoteitem_set.aggregate(models.Sum('price')).get('price__sum', 0)

    def sum_final_cost(self):
        return self.quoteitem_set.aggregate \
            (models.Sum('final_price')).get('final_price__sum', 0)


class QuoteItem(models.Model):
    quote = models.ForeignKey("Quote", on_delete=models.CASCADE, verbose_name='محصول')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="انتخاب دستگاه از لیست")
    discount = models.PositiveSmallIntegerField(verbose_name="درصد تخفیف")
    number = models.PositiveIntegerField(default=1, verbose_name="تعداد ")
    price = models.PositiveIntegerField(default=0, verbose_name="قیمت ")
    cost_with_tax = models.PositiveIntegerField(default=0, verbose_name="قیمت با مالیات")
    final_price = models.PositiveIntegerField(default=0, verbose_name="قیمت نهایی")

    class Meta:
        verbose_name = 'پیش فاکتور'
        verbose_name_plural = 'پیش فاکتورها'


class QuoteEmailHistory(models.Model):
    receiver = models.EmailField(verbose_name="ایمیل گیرنده")
    sent_email = models.BooleanField(default=False, verbose_name="ایمیل ارسال شد؟")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    user_sender = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="کاربر ارسال کننده")

    def __str__(self):
        return self.receiver


class QuoteFollowUp(models.Model):
    organization = models.ForeignKey('organization.Organization', verbose_name="سازمان", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    creator = models.ForeignKey(get_user_model(), verbose_name='کاربر ثبت کننده', on_delete=models.CASCADE)
    text = models.TextField(default=None, verbose_name='متن پیگیری')


class FollowUp(models.Model):
    organization = models.ForeignKey('organization.Organization', verbose_name="سازمان", on_delete=models.CASCADE)
    creator = models.ForeignKey(get_user_model(), verbose_name='کاربر ثبت کننده', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن پیگیری', default=None)

    class Meta:
        verbose_name = 'پیگیری'
        verbose_name_plural = 'پیگیری ها'
