from django.db import models
from organization_product.models import Product
# Create your models here.

class OrganizationMachin(models.Model):
    title = models.CharField(max_length=120, verbose_name='اسم ماشین ',null=True,blank=True)
    slug = models.SlugField(verbose_name='عنوان در url',null=True,blank=True)
    timestamp = models.DateTimeField(verbose_name='تاریخ ثبت',null=True,blank=True)
    active = models.BooleanField(default=True,null=True,blank=True, verbose_name='فعال / غیر فعال')
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ماشین'
        verbose_name_plural = 'ماشین آلات'
