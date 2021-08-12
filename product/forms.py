from django import forms
from product.models import Product


# <--------------------| فرم محصولات |-------------------->

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'tax', 'file_pdf', 'file_image', 'price', 'description', 'organization_product']
