from rest_framework import serializers
from .models import Product, Type, Price

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)
    price = PriceSerializer(read_only=True)

    type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(),
        source='type',
        write_only=True
    )
    price_id = serializers.PrimaryKeyRelatedField(
        queryset=Price.objects.all(),
        source='price',
        write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'type': {'required': False},
            'price': {'required': False},
        }