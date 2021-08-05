from django import forms
from quote import models


class QuoteForm(forms.ModelForm):
    class Meta:
        model = models.QuoteItem
        fields = ['quote', 'product', 'discount', 'number', 'price', 'cost_with_tax',
                  'final_price']
