from typing import Any
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.paginations import DefaultPagination
from store.models import Order, OrderItem
from store.serializers.order_serializer import OrderListSerializer, SaveOrderSerializer
from accounts.models import User
from store.services.order_service import OrderService

class OrderList(APIView, DefaultPagination):
    """
    List orders based on filters or create a new order
    """

    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.order_service = OrderService()

    def get(self, request):
        orders = Order.objects.all()
        paginated_orders = self.paginate_queryset(orders, request=request)
        if paginated_orders is not None:
            for order in paginated_orders:
                customer = User.objects.filter(id=order.user.id).first()
                setattr(order, 'customer', customer.get_full_name() if customer else "")
                setattr(order, 'customer_email', customer.email if customer else "")


        serializer = OrderListSerializer(paginated_orders, many=True)
        return self.get_paginated_response(serializer.data)
        
    
    def post(self, request):
        serializer = SaveOrderSerializer(data=request.data)
        if serializer.is_valid():
            response = self.order_service.save_order(data=serializer.validated_data,
                                                    customer=serializer.context['order_of_customer'],
                                                    author=request.user)
            if response['success']:
                return Response('Order created successfully', status=status.HTTP_201_CREATED)
            else:
                return Response('Something went wrong!', status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)