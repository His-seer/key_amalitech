# access_management/serializers.py
from rest_framework import serializers
from .models import AccessKey

class AccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessKey
        fields = ['id', 'user', 'status', 'date_of_procurement', 'expiry_date']
