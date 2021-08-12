from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = (
            'state',
            'name',
            'phone',
            'workers_qty',
            'organ_product',
            'full_name_owner',
            'phone_owner',
            'email_owner',
            'created_at',
            'user_creator',
        )