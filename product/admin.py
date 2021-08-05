from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'price', 'tax','file_pdf','file_image','description']
    search_fields = ('name', 'price','tax','description')
    list_filter = ('name', 'price','tax')
    list_editable = ['name', 'price','tax']

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
