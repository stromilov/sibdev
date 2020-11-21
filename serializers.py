#seiralizers.py

from rest_framework import serializers

from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    """Сериализатор покупателя"""
    class Meta:
        model = Deal
        fields = ('id', 'customer', 'total', 'quantity')