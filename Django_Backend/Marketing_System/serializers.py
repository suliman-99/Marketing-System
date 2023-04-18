from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'title', 'type', 'description']


class MarketerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketer
        fields = ['id', 'balance', 'withdrawal_threshold', 'commission', 'gender', 'reference_link']

