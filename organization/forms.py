from django import forms
from organization import models


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ['province_name','organization_name','organization_phone','organization_staff',
                  'manufacturedـproduct','personnel_name','personnel_mobile','personnel_email']