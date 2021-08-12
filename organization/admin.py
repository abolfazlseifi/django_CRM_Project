from django.contrib import admin
from . import models


# <--------------------| ادمین محصول سازمان |-------------------->

@admin.register(models.OrganizationProduct)
class OrganizationProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
    ]


# <--------------------| ادمین استان |-------------------->

@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
    ]


# <--------------------| ادمین  سازمان |-------------------->

@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = [
        'province_name', 'organization_name', 'organization_phone', 'organization_staff',
        'personnel_name', 'personnel_mobile', 'personnel_email', 'timestamp', 'creator'
    ]

    list_filter = ['province_name', 'organization_name', 'creator', ]

    list_display_links = ['organization_name', ]

    list_per_page = 5

    search_fields = ['organization_name__icontains']
