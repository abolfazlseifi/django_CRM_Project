from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'tax']
    search_fields = ('title', 'price','tax','description')
    list_filter = ('title', 'price','tax')
    list_editable = ['title', 'price','tax']

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
