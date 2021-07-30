from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']
    search_fields = ('title', 'price','active','description')
    list_filter = ('title', 'price','active')
    list_editable = ['title', 'price','active']

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
