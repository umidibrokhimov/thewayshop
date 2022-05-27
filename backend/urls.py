from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'backend'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('products/', Products.as_view(), name='products'),
    path('service/', OurService.as_view(), name='ourservice'),
    path('contact/', Contact.as_view(), name='contact'),

]