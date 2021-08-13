from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = (
            'province_name',
            'organization_name',
            'organization_phone',
            'organization_staff',
            'organization_product',
            'personnel_name',
            'personnel_mobile',
            'personnel_email',
            'timestamp',
            'creator',
        )