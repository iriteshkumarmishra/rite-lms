from rest_framework import serializers

from store.models import Product

class CartDataSerializer(serializers.Serializer):
    pass


class CartAddSerializer(serializers.Serializer):
    id = serializers.CharField()
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        product = Product.objects.filter(id=value).first()
        if not product:
            raise serializers.ValidationError('Product Not found')
        
        return value
    
    def get_product(self, object):
        return Product.objects.filter(id=object.product_id).first()


class CartItemSerailizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.FloatField()
    qty = serializers.IntegerField()
    display_price = serializers.CharField()


class CartDetailsSerializer(serializers.Serializer):
    id = serializers.CharField()
    items = serializers.ListField(child=CartItemSerailizer())
    settings = serializers.ListField()


class CartRemoveItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
