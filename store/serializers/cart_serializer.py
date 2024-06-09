from rest_framework import serializers

from store.models import Product

class CartDataSerializer(serializers.Serializer):
    pass


class CartAddSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    product_id = serializers.IntegerField()
    # product = serializers.SerializerMethodField()

    def validate_product_id(self, value):
        product = Product.objects.filter(id=value).first()
        if not product:
            raise serializers.ValidationError('Product Not found')
        
        return value
    
    def get_product(self, object):
        return Product.objects.filter(id=object.product_id).first()
    