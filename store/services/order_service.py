from django.db import transaction

from store.models import Order, OrderItem, Product
from accounts.models import UserAddress

class OrderService():

    def get_order_object(self, pk):
        order = Order.objects.filter(id=pk).first()
        return order
    
    def get_order_details(self, order, id=None):
        if id and not order:
            order = self.get_order_object(id)
        
        response = {
            'id': order.id, # type: ignore
            'test_order': order.test_order, # type: ignore
            'created_at': order.created_at, # type: ignore
            'status': order.status, # type: ignore
            'customer_id': order.user_id, # type: ignore
            'billing_address_id': order.billing_address_id, # type: ignore
            'tax': order.tax, # type: ignore
            'total': order.total, # type: ignore
            'sub_total': order.sub_total, # type: ignore
            'coupon_used': order.coupon_used, # type: ignore
            'order_items': list(order.item_order.all()) # type: ignore
        }

        # forming the billing_address for the response
        billing_address_object = order.billing_address # type: ignore
        order_billing_address = {
            'id' : billing_address_object.id,
            'is_default' : billing_address_object.is_default,
            'full_name' : billing_address_object.full_name,
            'address_line_1' : billing_address_object.address.address_line_1,
            'address_line_2' : billing_address_object.address.address_line_1,
            'zip' : billing_address_object.address.zip,
            'city' : billing_address_object.address.city,
            'state' : billing_address_object.address.state,
            'country' : billing_address_object.address.country,
        }
        response['billing_address'] = order_billing_address

        return response


    def save_order(self, data, customer, author):
        response = {
            'success': True,
            'order': None,
        }

        try:
            order = Order()
            with transaction.atomic():
                billing_address = UserAddress.objects.get(pk=data.get('billing_address_id'))
                order.status = data.get('status')
                order.user = customer
                order.billing_address = billing_address

                # calculating the whole amount now
                subtotal_amount = 0
                tax_amount = 0
                for item in data['order_items']:
                    subtotal_amount += item['total']
                
                order.sub_total = subtotal_amount
                order.tax = tax_amount # for now considering tax as 0
                order.total = subtotal_amount + tax_amount
                order.created_by = author
                order.updated_by = author
                order.save()

                # now saving order items for the above saved order
                for item in data['order_items']:
                    product = Product.objects.get(pk=item['product_id'])
                    order_item = OrderItem()
                    order_item.order = order
                    order_item.product = product
                    order_item.qty = item['quantity']
                    order_item.price_per_qty = item['price']
                    order_item.item_total = item['total']
                    order_item.created_by = author
                    order_item.save()

            response['order'] = order
            
        except Exception as e:
            response['success'] = False
            print(e)
        
        return response


    def update_order(self, data, order, author):
        pass