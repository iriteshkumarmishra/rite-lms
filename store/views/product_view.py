from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from store.models import Product
from core.paginations import DefaultPagination
from store.serializers.product_serializer import ProductListSerializer, ProductSaveSerializer
from accounts.models import User
from store.services.product_service import ProductService

class ProductList(APIView, DefaultPagination):
    """
    List all store products or create a new product
    """

    permission_classes = [IsAuthenticated, ]

    def __init__(self):
        self.product_service = ProductService()

    def get(self, request):
        products = Product.objects.all()
        paginated_result = self.paginate_queryset(products, request)
        response = []
        if paginated_result is not None:
            for data in paginated_result:
                user = User.objects.get(pk=data.created_by_id)
                setattr(data, 'author', user.first_name + ' ' + user.last_name)
                response.append(data)
        serializer = ProductListSerializer(response, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = ProductSaveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            response = self.product_service.create_product(serializer.validated_data, request.user)
            if response['success']:
                return Response('Product created', status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ProductDetails(APIView):
    """
    Retrieve, Update or Delete a product
    """

    permission_classes = [IsAuthenticated, ]

    def __init__(self):
        self.product_service = ProductService()

    def get(self, request, pk):
        product = self.product_service.get_product(pk)
        if product is None:
            raise Http404
        
        # fetch the related produ courses
        product_courses = product.course_product.all()
        temp_pcs = []
        for pcs in product_courses:
            temp_pcs.append(pcs.course_id)

        setattr(product, 'courses', temp_pcs)
        serializer = ProductSaveSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        product = self.product_service.get_product(pk)
        if product is None:
            raise Http404
        serializer = ProductSaveSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        response = self.product_service.update_product(product, serializer.validated_data, request.user)
        if response['success']:
            return Response('Product Updated', status=status.HTTP_202_ACCEPTED)
        
        return Response('Something went wrong!', status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.product_service.get_product(pk)
        if product is not None:
            product.delete()
            return Response('Product deleted', status=status.HTTP_204_NO_CONTENT)
        
        return Response('Something went wrong', status=status.HTTP_400_BAD_REQUEST)
        
        

    