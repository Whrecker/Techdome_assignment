from rest_framework import serializers
from .models import Customers, Admin

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
