from django import forms
from . import models
from django.forms import modelformset_factory

# <--------------------| فرم پیش فاکتور |-------------------->

QuoteItemCreateFormSet = modelformset_factory(models.QuoteItem, fields=('product', 'price', 'number', 'discount'),
                                              extra=1)


# <--------------------| فرم پیگیری |-------------------->

class FollowUpForm(forms.ModelForm):
    class Meta:
        model = models.FollowUp
        fields = ['text']
