from rest_framework import serializers

from accounts.models import User


class OrderListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.IntegerField()
    total = serializers.DecimalField(max_digits=5, decimal_places=2)
    test_order = serializers.BooleanField()
    customer = serializers.CharField()
    customer_email = serializers.EmailField()
    created_at = serializers.DateTimeField()


class OrderDetailSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField(required=False)
    status = serializers.ChoiceField(choices=[1, 2, 3, 4, 5])
    customer_id = serializers.IntegerField()
    billing_address_id = serializers.IntegerField()


class OrderItemDetailSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_title = serializers.CharField(max_length=255, required=False)
    quantity = serializers.IntegerField(default=1)
    price = serializers.DecimalField(decimal_places=2, max_digits=5)
    total = serializers.DecimalField(decimal_places=2, max_digits=5)



class SaveOrderSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[1, 2, 3, 4, 5])
    customer_id = serializers.IntegerField()
    billing_address_id = serializers.IntegerField()
    order_items = serializers.ListField(child=OrderItemDetailSerializer(), min_length=1)

    def validate_customer_id_field(self, value):
        customer = User.objects.filter(id=value).first()
        if customer is None:
            raise serializers.ValidationError('wrong customer passed')
        
        self.context['order_of_customer'] = customer

        return value
