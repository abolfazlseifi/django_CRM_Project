from django.db import models
# from product.models import Product

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150,null=True, verbose_name='عنوان در URL')
    # product = models.ManyToManyField(Product,blank=True,verbose_name='محصولات')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
