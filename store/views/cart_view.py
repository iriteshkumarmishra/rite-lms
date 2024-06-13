from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from store.models import Product
from store.services.cart_service import CartService

from store.serializers.cart_serializer import CartAddSerializer, CartDetailsSerializer, CartRemoveItemSerializer

class AddToCart(APIView):
    """
    Add an item to your cart
    """

    def __init__(self):
        self.cart_service = CartService()


    def post(self, request):
        serializer = CartAddSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        cart = self.cart_service.add_to_cart(serializer.validated_data)
        if cart['success']:
            return Response('Item added to cart')
        
        return Response(cart['message'], status=status.HTTP_200_OK)




class CartDetails(APIView):
    """
    Retrieve cart or delete items from cart
    """

    def __init__(self):
        self.cart_service = CartService()

    def get(self, request, pk):
        cart = self.cart_service.get_cart(pk)
        cart_contents = self.cart_service.get_cart_content(cart=cart)
        response = {
            'id': cart.id,
            'items': cart_contents['items'],
            'settings': cart_contents['settings'],
        }
        serializer = CartDetailsSerializer(response)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = CartRemoveItemSerializer(data=request.data)
        if serializer.is_valid():
            cart = self.cart_service.get_cart(pk)
            self.cart_service.remove_item_from_cart(cart=cart, item_id=serializer.validated_data.get('item_id'))
            return Response('Item removed from cart', status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)