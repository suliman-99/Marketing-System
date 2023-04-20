from rest_framework import serializers
from .models import *

class GetSmallProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'title', 'type', 'description']


class GetMarketerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketer
        fields = ['user_id', 'username', 'first_name', 'last_name', 'balance', 'withdrawal_threshold', 'commission', 'gender', 'reference_link', 'can_withdraw', 'products']

    user_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    can_withdraw = serializers.SerializerMethodField(method_name='get_can_withdraw')

    products = GetSmallProductSerializer(many=True, read_only=True)

    def get_can_withdraw(self, marketer: Marketer):
        return marketer.balance >= marketer.withdrawal_threshold

# --------------------------------------------------------------------------

class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'title', 'type', 'description']
    


