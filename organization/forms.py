from django import forms
from organization import models


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ['province_name','organization_name','organization_phone','organization_staff',
                  'organization_product', 'personnel_name', 'personnel_mobile', 'personnel_email']


class OrganizationProductForm(forms.ModelForm):
    class Meta:
        model = models.OrganizationProduct
        fields = ['name']