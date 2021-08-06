from django.db import models
from django.core.validators import FileExtensionValidator


def upload_image_path(file,path):
    return 'Product/Images'


def upload_pdf_path(file,path):
    return 'Product/PDFs'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم محصول', null=True)
    price = models.PositiveIntegerField(verbose_name='قیمت')
    tax = models.BooleanField(default=False, verbose_name='مشمول مالیات')
    file_pdf = models.FileField(upload_to='Product/PDFs', verbose_name='کاتولوگ محصول', blank=True,
                                validators=[FileExtensionValidator(['pdf'])] )
    file_image = models.ImageField(upload_to='Product/Images', verbose_name='تصویر محصول', blank=True)

    description = models.TextField(verbose_name='ویژگی های فنی')

    organization_product = models.ManyToManyField('organization.OrganizationProduct', blank=True,
                                                  verbose_name='قابل استفاده برای تولید محصولات تولیدی')



    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return f"/products/{self.id}/{self.name.replace(' ', '-')}"
