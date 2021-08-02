from django import forms
from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'tax', 'file_pdf', 'file_image', 'price', 'description', 'organization_product']
