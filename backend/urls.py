from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'backend'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('products/', ProductsList, name='products'),
    path('service/', OurService.as_view(), name='ourservice'),
    path('contact/', Contact.as_view(), name='contact'),
    path('cart/', ProductCart.as_view(), name='cart'),
    path('accounts/<int:pk>/', UserAccount.as_view(), name='account'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('check/', ProductCheckout.as_view(), name='product_checkout'),
    path('saved/', Wishlist.as_view(), name='liked_products'),
]