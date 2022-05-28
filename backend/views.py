from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *

class Home(ListView):
    context_object_name = 'categories'
    queryset = Categories.objects.all()
    template_name = 'index.html'

    def get_queryset(self):
        return HomeSlides.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['slides'] = HomeSlides.objects.all()
        return context


class About(ListView):
    context_object_name = 'teammembers'
    queryset = TeamMembers.objects.all()
    template_name = 'about.html'

class Products(TemplateView):
    template_name = 'shop.html'

class OurService(TemplateView):
    template_name = 'service.html'

class Contact(TemplateView):
    template_name = 'contact-us.html'