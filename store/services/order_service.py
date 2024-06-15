from django.db import transaction

from store.models import Order, OrderItem, Product

class OrderService():

    def get_orders(self, filters):
        pass

    def save_order(self, data, customer, author):
        response = {
            'success': True,
            'order': None,
        }

        try:
            order = Order()
            with transaction.atomic():
                order.status = data.get('status')
                order.user = customer
                order.billing_address = 1 # Need to change this

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
        
        return response
