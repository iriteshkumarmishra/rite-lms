from django.urls import path

from store.views.product_view import ProductList, ProductDetails
from store.views.cart_view import AddToCart, CartDetails
from store.views.order_view import OrderList

urlpatterns = [
    path('products/', ProductList.as_view(), name='products-list'),
    path('products/<int:pk>', ProductDetails.as_view(), name='products-details'),

    path('orders/', OrderList.as_view(), name='orders-list'),
    path('orders/<int:pk>', ProductList.as_view(), name='orders-details'),

    path('cart/', AddToCart.as_view(), name='cart-add'),
    path('cart/<str:pk>', CartDetails.as_view(), name='cart-details'),


]