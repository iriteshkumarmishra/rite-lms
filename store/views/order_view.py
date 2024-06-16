from typing import Any
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.paginations import DefaultPagination
from store.models import Order, OrderItem
from store.serializers.order_serializer import OrderListSerializer, SaveOrderSerializer, OrderDetailSerializer, UpdateOrderSerializer
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


class OrderDetails(APIView):
    """
    Retrieve, update or archive an order
    """

    permission_classes = [IsAuthenticated, ]

    def __init__(self):
        self.order_service = OrderService()

    def get(self, request, pk):
        order = self.order_service.get_order_object(pk)
        if order is None:
            return Response('Order not found', status=status.HTTP_404_NOT_FOUND)
        
        order_details = self.order_service.get_order_details(order=order)
        serializer = OrderDetailSerializer(order_details)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):        
        serializer = UpdateOrderSerializer(data=request.data, context= {'pk': pk})
        if serializer.is_valid():
            self.order_service.update_order(
                data=serializer.validated_data,
                order=serializer.context['order'],
                author=request.user)
            return Response('Order updated', status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, pk):
        pass
