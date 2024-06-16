from rest_framework import serializers

from accounts.models import User
from accounts.serializers import BillingAddressDetailsSerializer
from store.models import Order


class OrderListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.IntegerField()
    total = serializers.DecimalField(max_digits=5, decimal_places=2)
    test_order = serializers.BooleanField()
    customer = serializers.CharField()
    customer_email = serializers.EmailField()
    created_at = serializers.DateTimeField()



class OrderItemDetailSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_title = serializers.CharField(max_length=255, required=False)
    quantity = serializers.IntegerField(default=1)
    price_per_qty = serializers.DecimalField(decimal_places=2, max_digits=5)
    item_total = serializers.DecimalField(decimal_places=2, max_digits=5)



class SaveOrderSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[1, 2, 3, 4, 5])
    customer_id = serializers.IntegerField()
    billing_address_id = serializers.IntegerField()
    order_items = serializers.ListField(child=OrderItemDetailSerializer(), min_length=1)

    def validate_customer_id(self, value):
        customer = User.objects.filter(id=value).first()
        if customer is None:
            raise serializers.ValidationError('wrong customer passed')
        
        self.context['order_of_customer'] = customer

        return value


class OrderDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    created_at = serializers.DateTimeField()
    status = serializers.ChoiceField(choices=[1, 2, 3, 4, 5])
    coupon_used = serializers.CharField()
    customer_id = serializers.IntegerField()
    billing_address_id = serializers.IntegerField()
    tax = serializers.DecimalField(decimal_places=2, max_digits=5)
    test_order = serializers.BooleanField()
    total = serializers.DecimalField(decimal_places=2, max_digits=5)
    sub_total = serializers.DecimalField(decimal_places=2, max_digits=5)
    currency = serializers.CharField(default='USD', max_length=5)
    billing_address = BillingAddressDetailsSerializer(many=False)
    order_items = serializers.ListField(child=OrderItemDetailSerializer(), min_length=1)


class UpdateOrderSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[1, 2, 3, 4, 5])
    customer_id = serializers.IntegerField()
    billing_address_id = serializers.IntegerField()
    order_items = serializers.ListField(child=OrderItemDetailSerializer(), min_length=1)

    def validate(self, object):
        customer = User.objects.filter(id=object.get('customer_id')).first()
        if customer is None:
            raise serializers.ValidationError('wrong customer passed')
        
        self.context['order_of_customer'] = customer

        order = Order.objects.filter(id=self.context['pk']).first()
        if order is None:
            raise serializers.ValidationError('Order not found')
        
        if order.status != Order.STATUS_PAYMENT_PENDING:
            raise serializers.ValidationError('Order can\'t be updated')
        
        if order.user_id != object.get('customer_id'):
            raise serializers.ValidationError('Customer of order can\'t be changed')

        
        self.context['order'] = order

        return object
    