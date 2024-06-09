from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from store.models import Product
from store.services.cart_service import CartService

from store.serializers.cart_serializer import CartAddSerializer

class AddToCart(APIView):
    """
    Add an item to your cart
    """

    def __init__(self):
        self.cart_service = CartService()


    def post(self, request):
        serializer = CartAddSerializer(data=request.data, )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        cart = self.cart_service.add_to_cart(serializer.validated_data)
        if cart['success']:
            return Response('Item added to cart')
        
        return Response(cart['message'], status=status.HTTP_200_OK)




class CartDetails(APIView):
    pass