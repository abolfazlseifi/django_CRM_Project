from django.contrib import admin
from organization.models import Organization
# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['province_name','organization_name','organization_phone','organization_staff'
                    ,'personnel_name','personnel_mobile','personnel_email']

    search_fields = ('province_name','organization_name','organization_phone','organization_staff',
                  'manufacturedـproduct','personnel_name','personnel_mobile','personnel_email')

    list_filter = ('province_name','organization_name','personnel_name')

    list_editable = ['organization_phone','personnel_mobile','personnel_email']

    class Meta:
        model = Organization

admin.site.register(Organization, OrganizationAdmin)


