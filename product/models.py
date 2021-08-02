from django.db.models import Q
from django.db import models
import os


# from product_category.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_pdf_path(instance, filename):
    name, ext = get_filename_ext(filename)
    if ext == 'pdf':
        final_name = f"{instance.id}-{instance.title}{ext}"
        return f"products/{final_name}"


class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().all()

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='اسم دستگاه')
    price = models.IntegerField(verbose_name='قیمت')
    tax = models.BooleanField(default=False, verbose_name='مشمول مالیات')
    file_pdf = models.FileField(upload_to=upload_pdf_path, blank=True,
                                null=True, verbose_name='فایل کاتالوگ(PDF)')
    file_image = models.ImageField(upload_to=upload_image_path, blank=True, null=True,
                                   verbose_name='عکس کاتالوگ(jpeg)')

    description = models.TextField(verbose_name='ویژگی های فنی')

    organization_product = models.ManyToManyField('organization.OrganizationProduct', blank=True,
                                                  verbose_name='قابل استفاده برای تولید محصولات تولیدی')

    objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"
