
from store.models import Product, Cart

class CartService():

    def get_cart(self, id):
        cart = Cart.objects.get_or_create(id=id)
        return cart

    def add_to_cart(self, data):
        response = {
            'success': True,
            'message': 'Item added to cart'
        }
        cart = self.get_cart(data.get('user_id'))
        item = self.get_cart_item(cart, data.get('product_id'))
        if item:
            response['success'] = False
            response['message'] = 'Item already added to cart'
        else:
            
            self._add_to_cart(cart, data.get('product_id'))

        return response

    def get_cart_item(self, cart, item_id):
        pass # define thie method


    def _add_to_cart(self, cart, product_id):
        product = Product.objects.get(pk=product_id)
        cart_data = {
            'id': product.id,
            'name': product.title,
            'price': product.sale_price,
            'quantity': 1
        }
        cart.cart_data = cart.cart_data.append(cart_data)
        cart.save()    