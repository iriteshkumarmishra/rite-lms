
from store.models import Product, Cart
import json

from store.services.product_service import ProductService

class CartService():

    def get_cart(self, id):
        cart, created = Cart.objects.get_or_create(id=id) # return tuple (object, created_bool)
        return cart

    def add_to_cart(self, data):
        response = {
            'success': True,
            'message': 'Item added to cart'
        }
        cart = self.get_cart(data.get('id'))
        item = self.get_cart_item(cart, data.get('product_id'))
        if item:
            response['success'] = False
            response['message'] = 'Item already added to cart'
        else:
            self._add_to_cart(cart, data.get('product_id'))

        return response

    def get_cart_item(self, cart, item_id):
        # iterate all items to match item_id
        cart_data = json.loads(cart.cart_data if cart.cart_data else '[]')
        for item in cart_data:
            if item.get('id') == item_id:
                return item
        
        return None

    def _add_to_cart(self, cart, product_id):
        product = Product.objects.get(pk=product_id)
        cart_data = {
            'id': product.id,
            'name': product.title,
            'price': float(product.get_price()),
            'quantity': 1
        }

        data = json.loads(cart.cart_data if cart.cart_data else '[]')
        data.append(cart_data)
        cart_data = json.dumps(data)
        cart.cart_data = cart_data
        cart.save()
    

    def get_cart_content(self, id=None, cart=None):
        if id is not None:
            cart = self.get_cart(id)
        
        product_service = ProductService()
        # getting all items
        items = json.loads(cart.cart_data if cart.cart_data else '[]')
        item_response = []
        for item in items:
            product = product_service.get_product(item['id'])
            if product is None:
                continue

            temp_response = {
                'id': item['id'],
                'name': product.title,
                'price': item['price'],
                'qty': item['quantity'],
                'display_price': product.get_display_price(),
            }
            item_response.append(temp_response)
        
        # getting cart settings
        settings = json.loads(cart.cart_settings if cart.cart_settings else '{}')

        return {
            'items': item_response,
            'settings': settings,
        }
    
    def remove_item_from_cart(self, item_id, cart_id=None, cart=None):
        if cart_id is not None:
            cart = self.get_cart(cart_id)
        
        items = json.loads(cart.cart_data if cart.cart_data else '[]')
        for index, item in enumerate(items):
            print(index, item)
            if item.get('id') == item_id:
                items.pop(index)
                break
        
        cart_items = json.dumps(items)
        cart.cart_data = cart_items
        cart.save()
