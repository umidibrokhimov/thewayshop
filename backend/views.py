from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Products(TemplateView):
    template_name = 'shop.html'

class OurService(TemplateView):
    template_name = 'service.html'

class Contact(TemplateView):
    template_name = 'contact-us.html'